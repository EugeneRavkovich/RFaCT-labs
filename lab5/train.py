"""This module implements data feeding and training loop to create model
to classify X-Ray chest images as a lab example for BSU students.
"""

__author__ = 'Alexander Soroka, soroka.a.m@gmail.com'
__copyright__ = """Copyright 2020 Alexander Soroka"""

import argparse
import glob
import math

import numpy as np
import tensorflow as tf
import time
from tensorflow.python import keras as keras
from tensorflow.python.keras.callbacks import LearningRateScheduler
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers.experimental import preprocessing
from tensorflow.keras.models import Sequential
import csv


# Avoid greedy memory allocation to allow shared GPU usage
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

LOG_DIR = 'logs'
BATCH_SIZE = 32
NUM_CLASSES = 20
RESIZE_TO = 224
TRAIN_SIZE = 12786


# def logs_counter(func):
#
#     def wrapper():
#         return func
#     print(wrapper())
#     for key, value in wrapper().items():
#         loggs[key].append(value)
#
#     print(loggs)
#
#     return wrapper


class CustomCallback(tf.keras.callbacks.Callback):
    loggs = {'loss': [],
             'categorical_accuracy': [],
             'val_loss': [],
             'val_categorical_accuracy': [],
             }

    def on_epoch_end(self, epoch, logs=None):
        for key, value in logs.items():
            self.loggs[key].append(value)
        print(logs)


def to_log_file(logs, logdir):
    with open(logdir, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('epoch', 'loss', 'categorical_accuracy', 'val_loss', 'val_categorical_accuracy'))

        for i in range(len(logs['loss'])):
            writer.writerow(((i+1), logs['loss'][i], logs['categorical_accuracy'][i], logs['val_loss'][i],
                             logs['val_categorical_accuracy'][i]))


def parse_proto_example(proto):
    keys_to_features = {
        'image/encoded': tf.io.FixedLenFeature((), tf.string, default_value=''),
        'image/label': tf.io.FixedLenFeature([], tf.int64, default_value=tf.zeros([], dtype=tf.int64))
    }
    example = tf.io.parse_single_example(proto, keys_to_features)
    example['image'] = tf.image.decode_jpeg(example['image/encoded'], channels=3)
    example['image'] = tf.image.convert_image_dtype(example['image'], dtype=tf.uint8)
    example['image'] = tf.image.resize(example['image'], tf.constant([250, 250]))
    return example['image'], tf.one_hot(example['image/label'], depth=NUM_CLASSES)


def aug_images(image, label):
    temp = tf.image.adjust_contrast(image, 2)
    temp = tf.image.adjust_brightness(temp, 0.3)
    return tf.image.random_crop(temp, [224, 224, 3]), label


def create_dataset(filenames, batch_size):
    """Create dataset from tfrecords file
    :tfrecords_files: Mask to collect tfrecords file of dataset
    :returns: tf.data.Dataset
    """
    return tf.data.TFRecordDataset(filenames) \
        .map(parse_proto_example, num_parallel_calls=tf.data.AUTOTUNE) \
        .cache() \
        .map(aug_images) \
        .batch(batch_size) \
        .prefetch(tf.data.AUTOTUNE)


def build_model():
    inputs = tf.keras.Input(shape=(RESIZE_TO, RESIZE_TO, 3))
    temp = tf.keras.layers.experimental.preprocessing.RandomRotation(factor=0.01)(inputs)
    temp = tf.keras.layers.GaussianNoise(0.005)(temp)
    model = tf.keras.applications.EfficientNetB0(include_top=False, input_tensor=temp, weights='imagenet')
    model.trainable = False
    x = tf.keras.layers.GlobalAveragePooling2D()(model.output)
    outputs = tf.keras.layers.Dense(NUM_CLASSES, activation=tf.keras.activations.softmax)(x)
    return tf.keras.Model(inputs=inputs, outputs=outputs)


def unfreeze_model(model):
    # We unfreeze the top 20 layers while leaving BatchNorm layers frozen
    for layer in model.layers:
        if not isinstance(layer, tf.keras.layers.BatchNormalization):
            layer.trainable = True


def step_decay(epoch):
    initial_lrate = 0.001
    drop = 0.3
    epochs_drop = 4.0
    l_rate = initial_lrate * math.pow(drop, math.floor((1 + epoch) / epochs_drop))
    print('learning rate = {}'.format(l_rate))
    return l_rate


def main():
    args = argparse.ArgumentParser()
    args.add_argument('--train', type=str,
                      help='Glob pattern to collect train tfrecord files, use single quote to escape *')
    args = args.parse_args()

    dataset = create_dataset(glob.glob(args.train), BATCH_SIZE)
    train_size = int(TRAIN_SIZE * 0.7 / BATCH_SIZE)
    train_dataset = dataset.take(train_size)
    validation_dataset = dataset.skip(train_size)

    l_rate = LearningRateScheduler(step_decay)
    model = build_model()
    model.compile(
        optimizer=tf.optimizers.Adam(),
        loss=tf.keras.losses.categorical_crossentropy,
        metrics=[tf.keras.metrics.categorical_accuracy],
    )

    log_dir = '{}/owl-{}.csv'.format(LOG_DIR, time.time())
    model.fit(
        train_dataset,
        epochs=2,
        validation_data=validation_dataset,
        callbacks=[
            CustomCallback(),
            l_rate
        ]
    )

    unfreeze_model(model)

    model.compile(
        optimizer=tf.optimizers.Adam(0.0000001),
        loss=tf.keras.losses.categorical_crossentropy,
        metrics=[tf.keras.metrics.categorical_accuracy],
    )
    model.fit(
        train_dataset,
        epochs=2,
        validation_data=validation_dataset,
        callbacks=[
            CustomCallback(),
        ]
    )
    to_log_file(CustomCallback.loggs, log_dir)
    print(CustomCallback.loggs)

if __name__ == '__main__':
    main()

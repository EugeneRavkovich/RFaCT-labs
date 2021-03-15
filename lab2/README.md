# 1. Обучить нейронную сеть EfficientNet-B0 (случайное начальное приближение) для решения задачи классификации изображений Oregon Wildlife   
* **Описание архитетуры:**   
  ```
  def build_model():
  inputs = tf.keras.Input(shape=(RESIZE_TO, RESIZE_TO, 3))
  outputs = tf.keras.applications.EfficientNetB0(include_top=True, weights=None, classes=NUM_CLASSES)(inputs)
  return tf.keras.Model(inputs=inputs, outputs=outputs)
  ```
* **Графики обучения:**  
  *Синяя линия - на валидации*   
  *Оранжевая линия - на обучении*   
  * Визуализация выбранной метрики качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/random_epoch_categorical_accuracy.svg)
  * Визуализация выбранной функции потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/random_epoch_loss.svg)    
# 2. С использованием техники обучения Transfer Learning обучить нейронную сеть EfficientNet-B0 (предобученную на базе изображений imagenet) для решения задачи классификации изображений Oregon Wildlife   
* **Описание архитектуры:**
  ```
  def build_model():
  inputs = tf.keras.Input(shape=(RESIZE_TO, RESIZE_TO, 3))
  model = tf.keras.applications.EfficientNetB0(include_top=False, input_tensor=inputs, weights='imagenet')
  model.trainable = False
  x = tf.keras.layers.GlobalAveragePooling2D()(model.output) # (None x H x W x channels --> None x channels(1280))
  outputs = tf.keras.layers.Dense(NUM_CLASSES, activation=tf.keras.activations.softmax)(x)
  return tf.keras.Model(inputs=inputs, outputs=outputs)
  ```
  * **Графики обучения:**  
  *Синяя линия - на валидации*   
  *Оранжевая линия - на обучении*   
  * Визуализация выбранной метрики качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/imagenet_epoch_categorical_accuracy.svg)
  * Визуализация выбранной функции потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/imagenet_epoch_loss.svg)
* **Анализ полученных результатов**   
  В обоих случаях получились отвратительные результаты. В замечаниях к методичке указано о необходимости выполнения стандартизации или нормирования данных, а так же о том, что нужно обратить внимание на размер и тип данных входных изображений, но, если я правильно понял, это уже выполнено в коде ниже:
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/pics/1.png)
  В целом, все мои попытки что-то предпринять не увенчались успехом. Поэтому я решил адаптировать и прогнать код с https://keras.io/examples/vision/image_classification_efficientnet_fine_tuning/ на нашем датасете. Результаты получились следующие:    
  # Transfer Learning:   
  *Синяя линия - на валидации*   
  *Оранжевая линия - на обучении*   
  * Визуализация выбранной метрики качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/my_imagenet_epoch_categorical_accuracy.svg)
  * Визуализация выбранной функции потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/my_imagenet_epoch__loss.svg)

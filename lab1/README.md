
# 1. С использованием примера[1] обучить представленную реализацию нейронной сети для решения задачи классификации изображений Oregon-Wild-Life
* **Описание архитектуры:**   
  * input.shape TensorShape([None, 224, 224, 3])
  ```
  inputs = tf.keras.Input(shape=(RESIZE_TO, RESIZE_TO, 3))
  ```
  * Конволюционный слой с 8-ю фильтрами и ядром 3х3    
    TensorShape([None, 222, 222, 8])
  ```
  x = tf.keras.layers.Conv2D(filters=8, kernel_size=3)(inputs)
  ```
  * Операция MaxPool2d(2х2)      
  Выбор максимального значения в окне 2х2     
  TensorShape([None, 111, 111, 8])
  ```
  x = tf.keras.layers.MaxPool2D()(x)
  ```
  * Приведение тензора с размерностью TensorShape([None, 111, 111, 8]) в тензор размерности TensorShape([None, 98568])    
  ```
  x = tf.keras.layers.Flatten()(x)
  ```
  Полносвязный слой с 20 выходами и функцией активации softmax, которая приводит результат к вероятностному виду    
  ```
  outputs = tf.keras.layers.Dense(NUM_CLASSES, activation=tf.keras.activations.softmax)(x)
  ```
* **Графики обучения**   
  *Синяя линия - на валидации*   
  *Оранжевая линия - на обучении*   
  * Визуализация выбранной метрики качества (categorical_accuracy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab1/graphs/accuracy1.png)
  * Визуализация выбранной функции потерь (categorical_crossentropy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab1/graphs/loss1.png)
* **Анализ полученных результатов**    
  Судя по графикам наблюдается переобучение тестируемой модели, что вызвано малым размером обучаеющей выборки и случайным начальным приближением. 
# 2.Создать и обучить сверточную нейронную сеть произвольной архитектуры с количеством сверточных слоев >3
* **Описание структуры**  
  * Добавлены слои BatchNormalization (чисто рецептурно)    
  * Добавлены функции активации Relu для большей нелинейности   
  ```
  x = tf.keras.layers.Conv2D(filters=16, kernel_size=4, strides=2, padding='same')(inputs) # 112 x 112 x 16
  x = tf.keras.layers.BatchNormalization()(x)
  x = tf.keras.activations.relu(x)
  x = tf.keras.layers.Conv2D(filters=32, kernel_size=4, strides=2, padding='same')(x) # 56 x 56 x 32
  x = tf.keras.layers.BatchNormalization()(x)
  x = tf.keras.activations.relu(x)
  x = tf.keras.layers.Conv2D(filters=64, kernel_size=4, strides=2, padding='same')(x) # 28 x 28 x 64
  x = tf.keras.layers.BatchNormalization()(x)
  x = tf.keras.activations.relu(x)
  x = tf.keras.layers.Conv2D(filters=128, kernel_size=4, strides=2, padding='same')(x) # 14 x 14 x 128
  x = tf.keras.layers.BatchNormalization()(x)
  x = tf.keras.activations.relu(x)
  x = tf.keras.layers.Conv2D(filters=256, kernel_size=4, strides=2, padding='same')(x) # 7 x 7 x 256
  x = tf.keras.layers.Flatten()(x)
  x = tf.keras.layers.Dense(256)(x)
  outputs = tf.keras.layers.Dense(NUM_CLASSES, activation=tf.keras.activations.softmax)(x)
  ```
* **Графики обучения**   
  *Синяя линия - на валидации*   
  *Оранжевая линия - на обучении*   
  * Визуализация выбранной метрики качества (categorical_accuracy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab1/graphs/accuracy2.png)
  * Визуализация выбранной функции потерь (categorical_crossentropy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab1/graphs/loss2.png)
* **Анализ полученных результатов**    
  В данном случае наблюдаются те же проблемы что и в прошлом; причины такие же. Помимо этого, с увеличением глубины нейронной сети ухудшилась ее обобщающая способность, что видно на графике метрики качества.  
  Применение BatchNormalization оказалось излишне, в силу накладываемых ограничений на использование, о которых я ранее не знал. Это также могло негативно сказаться на результате.    
  В целом, ~13тыс. картинок недостаточно для того чтобы качественно обучить нейронную сеть. В таком случае можно попробовать применить аугментацию данных, что позволит значительно увеличить объем обучающей выборки.
## Ссылки
#### 1. https://github.com/AlexanderSoroka/CNN-oregon-wildlife-classifier 


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
  Выбор максимального значения в окне 2х2 с последующим уменьшением матрицы признаков    
  TensorShape([None, 111, 111, 8])
  ```
  x = tf.keras.layers.MaxPool2D()(x)
  ```
  * Выравнивание матрицы признаков в тензор путем перемножения всех размерностей (111x111x8)    
  TensorShape([None, 98568])
  ```
  x = tf.keras.layers.Flatten()(x)
  ```
  Полносвязный слой с NUM_CLASSES выходами и функцией активации softmax, которая приводит результат к вероятностному виду    
  ```
  outputs = tf.keras.layers.Dense(NUM_CLASSES, activation=tf.keras.activations.softmax)(x)
  ```
* **Графики обучения**   
  *Синяя линия - на валидации*   
  *Оранжевая линия - на обучении*   
  * Визуализация выбранной метрики качества
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab1/graphs/accuracy1.png)
  * Визуализация потерь
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab1/graphs/loss1.png)
* **Анализ полученных результатов**   
## Ссылки
#### 1. https://github.com/AlexanderSoroka/CNN-oregon-wildlife-classifier 

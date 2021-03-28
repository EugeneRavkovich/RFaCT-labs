*Везде, кроме пункта \*, представлены графики для этапа валидации*    
*Базовый алгоритм (с которым будет происходить сравнение) - алгоритм с применением оптимальной политики изменения темпа обучения из предыдущей лабораторной работы*
# 1. С использованием техники обучения Transfer Learning и оптимальной политики изменения темпа обучения обучить нейронную сеть EfficientNet-B0 (предварительно обученную на базе изображений imagenet) для решения задачи классификации изображений Oregon Wildlife с использованием следующих техник аугментации данных: 
  ### 1) Манипуляции с яркостью и контрастом
  * Визуализация метрик качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab4/graphs/contrast%20%26%20brightness/contrast%26brightness_categorical_accuracy.png)
  * Визуализация функций потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab4/graphs/contrast%20%26%20brightness/contrast%26brightness_loss.png)
  #### Оптимальные параметры: фактор контраста - 2 и изменение яркости - 0.3. При такой комбинации достигается максимальное значение метрики качества на валидации и наилучшая скорость сходимости. Алгоритм с данным типом аугментации достиг предела сходимости на 24-й эпохе, в то время как базовый алгоритм достиг предела сходимости лишь на 30-й эпохе. Прирост качества - 0.36% относительно базового алгоритма.
  ### 2) Случайный поворот
  * Визуализация метрик качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab4/graphs/random%20rotation/random_rotation_categorical_accuracy.png)
  * Визуализация функций потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab4/graphs/random%20rotation/random_rotation_loss.png)    
  #### Влияние режима заполнения 
  * Визуализация метрик качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab4/graphs/random%20rotation/random_rotation_fill_modes_categorical_accuracy.png)
  * Визуализация функций потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab4/graphs/random%20rotation/random_rotation_fill_modes_loss.png)
  ### 3) Использование случайной части изображения
  * Визуализация метрик качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab4/graphs/random_crop/random_crop_categorical_accuracy.png)
  * Визуализация функций потерь 
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab4/graphs/random_crop/random_crop_loss.png)
  ### 4) Добавление случайного шума
  * Визуализация метрик качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab4/graphs/random_noise/random_noise_categorical_accuracy.png)
  * Визуализация функций потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab4/graphs/random_noise/random_noise_loss.png)
  #### Наилучший результат наблюдается при значении среднеквадратичного отклонения добавляемого шума, равном 0.1. Также, потребовалось внести изменения в настройки политики изменения темпа обучения и изменить начальное значение темпа обучения с 0.1 на 0.01. В результате текущий алгоритм достиг предела сходимости на 21-й эпохе с увеличение качества на валидации на 0.12% в сравнении с базовым алгоритмом.

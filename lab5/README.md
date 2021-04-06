# 1. С использованием техники обучения Transfer Learning, оптимальной политики изменения темпа обучения, аугментации данных с оптимальными настройками обучить нейронную сеть EfficientNet-B0 (предварительно обученную на базе изображений imagenet) для решения задачи классификации изображений Oregon WildLife
#### Используемые техники аугментации данных:    
* Манипуляции с яркостью и контрастом. Параметры: фактор контраста - 2, изменение яркости - 0.3
* Поворот изображения на случайный угол. Параметры: множитель угла поворота - 0.05, режим заполнения - 'constant', параметр заполнения - 255   
* Использование случайной части изображения. Размер изображения, передаваемого в метод - 250х250 пикселей
* Добавление случайного шума. Среднеквадратичное отклонение добавляемого шума - 0.01
### Графики для Transfer Learning
* Визуализация метрики качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab5/graphs/all_in_one_categorical_accuracy.png)
* Визуализация функции потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab5/graphs/all_in_one_loss.png)
# 2. С использованием техники обучения Fine Tuning дополнительно обучить нейронную сеть EfficientNet-B0 предварительно обученную в пункте 1
* Темп обучения на стадии Fine Tuning - 2e-7
### Графики для Fine Tuning
* Визуализация метрики качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab5/graphs/fine_tuning_categorical_accuracy.png)
* Визуализация функции потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab5/graphs/fine_tuning_loss.png)
# Анализ полученных результатов   
Использование техники обучения Fine Tuning не привело к увеличению качества, наоборот, качество ухудшилось на 0.03%

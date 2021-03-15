# 1. Обучить нейронную сеть EfficientNet-B0 (случайное начальное приближение) для решения задачи классификации изображений Oregon Wildlife   
* **Графики обучения:**  
  *Синяя линия - на валидации*   
  *Оранжевая линия - на обучении*   
  * Визуализация выбранной метрики качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/random_epoch_categorical_accuracy.svg)
  * Визуализация выбранной функции потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/random_epoch_loss.svg)    
  * **Анализ полученных результатов**    
  Судя по графикам можно сделать вывод, что модель очень плохо обучается, что может быть связано со случайным начальным приближением или низким шагом обучения.
# 2. С использованием техники обучения Transfer Learning обучить нейронную сеть EfficientNet-B0 (предобученную на базе изображений imagenet) для решения задачи классификации изображений Oregon Wildlife   
  * **Графики обучения:**  
  *Синяя линия - на валидации*   
  *Оранжевая линия - на обучении*   
  * Визуализация выбранной метрики качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/imagenet_epoch_categorical_accuracy.svg)
  * Визуализация выбранной функции потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/imagenet_epoch_loss.svg)
* **Анализ полученных результатов**   

  

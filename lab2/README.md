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
  На графиках видно, что применение техники transfer learning существенно увеличило качество классификации.При Learning rate 0.001 модель обучалась плохо:    
  *Синяя линия - на валидации*   
  *Оранжевая линия - на обучении*   
  * Визуализация выбранной метрики качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/imagenet_epoch_categorical_accuracy.svg)
  * Визуализация выбранной функции потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/imagenet_epoch_loss.svg)
  Понижение Learning rate до 0.0001 положительно сказалось на процессе обучения. 
## Прежде чем было принято решение понизить шаг обучения, я пытался адаптировать и прогнать код с https://keras.io/examples/vision/image_classification_efficientnet_fine_tuning/ , результaты ниже:
### Transfer Learning:   
  *файл efficientnetb0_w_imagenet.py*     
  *Синяя линия - на валидации*   
  *Оранжевая линия - на обучении*   
  * Визуализация выбранной метрики качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/my_imagenet_epoch_categorical_accuracy.svg)
  * Визуализация выбранной функции потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/my_imagenet_epoch__loss.svg)
  ### Случайное начальное приближение:    
  *На 27 эпохе вылезла ошибка 'out of memory', поэтому на графике не представлены все 50 эпох обучения*    
  *файл efficientnetb0_random_weights.py*     
  *Синяя линия - на валидации*   
  *Оранжевая линия - на обучении*   
  * Визуализация выбранной метрики качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/my_none_epoch_categorical_accuracy.svg)
  * Визуализация выбранной функции потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab2/graphs/my_none_epoch_loss.svg)

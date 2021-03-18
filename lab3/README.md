# 1. С использованием [1] и техники обучения Transfer Learning обучить нейронную сеть EfficientNet-B0 (предварительно обученную на базе изображений imagenet) для решения задачи классификации изображений Oregon Wildlife с использованием фиксированных темпов обучения 0.1, 0.01, 0.001, 0.0001     
   Представлены графики для этапа валидации
  * Визуализация метрики качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/lr_comparision/diff_LR_validation.categorical_accuracy.png)
  * Визуализация функции потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/lr_comparision/diff_LR_validation.loss.png)
  
  #### При learning rate 0.001 наблюдается наилучшее качество на валидации и наивысшая скорость обучения на заданом промежутке. Несмотря на небольшое переобучение (см. график ниже), его можно принять оптимальным. 
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/lr_comparision/lr_0.001_validation_overfitting.svg)
# 2. Step Decay
# 3. Exponential Decay
* Визуализация метрик качества (categorical_accuracy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/exp%20decay%20comparision/exp_decay_metric_comparision.png)
* Визуализация функций потерь (categorical_crossentropy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/exp%20decay%20comparision/exp_decay_loss_comparision.png)
   #### Оптимальные параметры в данном случае: initial_rate=0.1, k=0.3. Использование этих параметров приводит к уменьшению времени обучения и к наивысшему показателю метрики качества на валидации.
 # 4. Анализ полученных результатов
 

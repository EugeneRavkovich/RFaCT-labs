*Везде, кроме пункта \*, представлены графики для этапа валидации*
# 1. С использованием [1] и техники обучения Transfer Learning обучить нейронную сеть EfficientNet-B0 (предварительно обученную на базе изображений imagenet) для решения задачи классификации изображений Oregon Wildlife с использованием фиксированных темпов обучения 0.1, 0.01, 0.001, 0.0001     
  * Визуализация метрик качества (categorical_accuracy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/lr_comparision/diff_LR_validation.categorical_accuracy.png)
  * Визуализация функций потерь (categorical_crossentropy)
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/lr_comparision/diff_LR_validation.loss.png)
  #### При learning rate 0.001 наблюдается наилучшее качество на валидации и наивысшая скорость обучения на заданом промежутке. Несмотря на небольшое переобучение (см. график ниже), его можно принять оптимальным.    
  \*
  * Синяя линия - на обучении   
  * Оранжевая линия - на валидации
  ![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/lr_comparision/lr_0.001_overfittin.svg)
# 2. Step Decay
* Визуализация метрик качества (categorical_accuracy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/step%20decay%20comparision/step_decay_metric_comparision.png)
* Визуализация функций потерь (categorical_crossentropy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/step%20decay%20comparision/step_decay_loss_comparision.png)
 #### Оптимальные параметры: initial_rate=0.1, drop=0.4, epochs_drop=3. В случае применения политики Step Decay все из опробованных комбинаций параметров приводят к уменьшению времени обучения, а выбранная комбинация показывает наилучшее качество на валидации.
# 3. Exponential Decay
* Визуализация метрик качества (categorical_accuracy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/exp%20decay%20comparision/exp_decay_metric_comparision.png)
* Визуализация функций потерь (categorical_crossentropy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/exp%20decay%20comparision/exp_decay_loss_comparision.png)
   #### Оптимальные параметры в данном случае: initial_rate=0.1, k=0.3. Использование этих параметров приводит к уменьшению времени обучения и к наивысшему показателю метрики качества на валидации.
 # 4. Анализ полученных результатов
 * Визуализация метрик качества (categorical_accuracy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/fixed-step-exp%20comparision/fixed_step_exp_metric_comparision.png)
* Визуализация функций потерь (categorical_crossentropy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/fixed-step-exp%20comparision/fixed_step_exp_loss_comparision.png)
По финальным графикам видно, что применение политик изменения темпа обучения не дало значительного прироста в качестве (по крайней мере при опробованных параметрах), но достаточно ощутимо ускорило время обучения.
### Ссылки
https://github.com/AlexanderSoroka/CNN-oregon-wildlife-classifier

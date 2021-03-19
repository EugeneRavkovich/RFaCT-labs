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
 #### Оптимальные параметры: начальное значение темпа обучения - 0.1 со снижением в 0.4 раза каждые 3 эпохи. Выбранная комбинация параметров приводит к наивысшему значению метрики качества на валидации. Алгоритм достигает предела сходимости на 28-й эпохе с качеством в 89.22% и к концу обчения превосходит алгоритм с оптимальным фиксированным темпом обучения на 0.39%.
# 3. Exponential Decay
* Визуализация метрик качества (categorical_accuracy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/exp%20decay%20comparision/exp_decay_metric_comparision.png)
* Визуализация функций потерь (categorical_crossentropy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/exp%20decay%20comparision/exp_decay_loss_comparision.png)
   #### Оптимальные параметры в данном случае: начальное значение темпа обучения - 0.1 с фактором наклона экспоненциальной кривой 0.3. При такой комбинации достигается максимальное значение метрики качества на валидации в 89.17%. Алгоритм достигает предела сходимости на 30-й эпохе и к концу обучения превосходит алгоритм с оптимальным фиксированным темпом обучения на 0.34%.
 # 4. Анализ полученных результатов
 * Визуализация метрик качества (categorical_accuracy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/fixed-step-exp%20comparision/fixed_step_exp_metric_comparision.png)
* Визуализация функций потерь (categorical_crossentropy)
![Image alt](https://github.com/Mariwannaxsfzx/RFaCT-labs/blob/main/lab3/graphs/fixed-step-exp%20comparision/fixed_step_exp_loss_comparision.png)
По финальным графикам видно, что применение политик изменения темпа обучения не дало значительного прироста в качестве (по крайней мере при опробованных параметрах), но достаточно ощутимо ускорило сходимость алгоритма
### Ссылки
1. https://github.com/AlexanderSoroka/CNN-oregon-wildlife-classifier

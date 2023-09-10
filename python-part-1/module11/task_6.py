print('Задача 6. Ход конём')


# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
# 
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

import math

print('Введите местоположение коня:')
xCurrent = int(math.floor(float(input()) * 10))
yCurrent = int(math.floor(float(input()) * 10))
print('Введите местоположение точки на доске:')
xNext = int(math.floor(float(input()) * 10))
yNext = int(math.floor(float(input()) * 10))

print('Конь в клетке (' + str(xCurrent) + ', ' + str(yCurrent) + '). Точка в клетке (' + str(xNext) + ', ' + str(yNext) + ')')

if (xNext in range(8)) and (yNext in range(8)) and ((abs(xCurrent - xNext) == 2) and (abs(yCurrent - yNext) == 1)  or  ((abs(xCurrent - xNext) == 1) and (abs(yCurrent - yNext) == 2))):
  print('Да, конь может ходить в эту точку.')
else:
  print('Нет, конь не может ходить в эту точку.')




print('\n--------\n')
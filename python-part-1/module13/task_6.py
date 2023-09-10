print('Задача 6. Яйца')

# В рамках программы колонизации Марса
# компания «Спейс Инжиниринг» вывела особую породу черепах,
# которые, по задумке, должны размножаться, откладывая яйца в марсианском грунте.
# Откладывать яйца слишком близко к поверхности опасно из-за радиации,
# а слишком глубоко — из-за давления грунта и недостатка кислорода.
# Вообще, факторов очень много,
# но специалисты проделали большую работу и предположили,
# что уровень опасности для черепашьих яиц рассчитывается по формуле
# D = x**3 − 3x**2 − 12x + 10,
# где x — глубина кладки в метрах,
# а D — уровень опасности в условных единицах.
# 
# Для тестирования гипотезы
# нужно взять пробу грунта на безопасной, согласно формуле, глубине.
# 
# Напишите программу,
# находящую такое значение глубины "х", при котором уровень опасности как можно более близок к нулю.
# На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля,
# а программа должна рассчитать приблизительное значение "х",
# удовлетворяющее этому отклонению.
# 
# Известно, что глубина точно больше нуля и меньше четырёх метров.
# 
# Обеспечьте контроль ввода.
# 
# Пример:
# Введите максимально допустимый уровень опасности: 0.01
# 
# Приблизительная глубина безопасной кладки: 0.732421875 м
import math

def countMaxSafeDepth(dRate):
  # нахождение "x" сводится к решению кубического уравнения
  # x**3 − 3*x**2 − 12*x + 10 = dRate (или x**3 − 3*x**2 − 12*x + (10 - dRate) = 0)
  # это можно сделать с помощью формулы Виета-Кардано:
  x, x_1, x_2, x_3 = 0, 0, 0, 0
  a, b, c = -3, -12, (10 - dRate)
  q = (a ** 2 - 3 * b) / 9                          # 
  r = (2 * a ** 3 - 9 * a * b + 27 * c) / 54        # 
  s = q ** 3 - r ** 2                               # 
  fi = (math.acos(r / math.sqrt(q ** 3))) / 3

  # print('q =', q)
  # print('r =', r)
  # print('s =', s)   

  # если s > 0, то уравнение имеет три действительных корня
  if s > 0:
    x_1 = -2 * math.sqrt(q) * math.cos(fi) - a / 3                        # 
    x_2 = -2 * math.sqrt(q) * math.cos(fi + (2 * math.pi) / 3) - a / 3    # 
    x_3 = -2 * math.sqrt(q) * math.cos(fi - (2 * math.pi) / 3) - a / 3    # 
  else:
  # для решения уравнения в данном случае необходимо использовать не тригонометрические, а гиперболические функции (если s > 0) или сигнум-функцию (если s = 0)
    print('К сожалению, решение данной задачи требует значительно более расширенных знаний математики с участием специалиста в этой области более высокого уровня.')

  
  # print('x_1 =', x_1)
  # print('x_2 =', x_2)
  # print('x_3 =', x_3)   

  # по условию задачи глубина больше 0 и меньше 4-х метров, проверим все корни на это условие:
  if 0 < x_1 < 4:
    print('Приблизительная глубина безопасной кладки:', x_1, 'м')
  elif 0 < x_2 < 4:
    print('Приблизительная глубина безопасной кладки:', x_2, 'м')
  elif 0 < x_3 < 4:
    print('Приблизительная глубина безопасной кладки:', x_3, 'м')    
  else:
    print('К сожалению, решение не было найдено.')


acceptableRate = float(input('Введите максимально допустимый уровень опасности: '))
countMaxSafeDepth(acceptableRate)


print('Задача 7. Сумма ряда')

# Дано натуральное число N. Напишите программу для вычисления суммы N элементов последовательности по формуле 
# (-1)**n * 1/(2**n), где n — это порядковый номер элемента (расчёт начинается с нуля).

# Примеры расчётов

# При N = 4 элементы выражения будут равны:
# n = 0 
# elem = (−1) ** 0 * (½) ** 0 = 1      <<= elem = (−1) ** 0 * 1/(2**0) = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# Сумма равна:
# s=1- 12+14-18 = 5/8 = 0,625

# При N = 6 элементы выражения будут равны:
# n = 0 
# elem = (−1) ** 0 * (½) ** 0 = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# n = 4
# elem = (−1) ** 4 * (½) ** 4 = (1/16)  <<= ЗДЕСЬ НЕПОНЯТНО ПО КАКОМУ КРИТЕРИЮ ДРОБЬ 
# n = 5                                     ВЗЯТА В СКОБКИ. ПРЕДПОЛАГАЮ, ЧТО ПО ОШИБКЕ,  
# elem = (−1) ** 5 * (½) ** 5 = (−1/32)     Т.К. ДРОБЬ НЕОТРИЦАТЕЛЬНАЯ
# Сумма равна:
# s = 1 − ½ + ¼ − ⅛ + 1/16 − 1/32 = 21/32 = 0,65625

# P. S. Не стоит выполнять расчёты каждого элемента вручную, используйте цикл.

from fractions import Fraction

positive_int = int(input('Введите натуральное число: '))
summ = 0
# создадим список, где будем хранить элементы в виде десятичных дробей
elem_list = list()
print('При N =', positive_int, 'элементы выражения будут равны:')
for n in range(positive_int):
  print()
  print('n =', n)
  elem = (-1) ** n * 1 /(2 ** n)

  # чтобы результат вывода соответствовал условию, преобразуем десятичные дроби в обычные и отрицательные дроби возьмем в скобки
  if elem < 0:
    elem_string_brac = '(' + str(Fraction(elem)) + ')'
  else:
    elem_string_brac = str(Fraction(elem))
  # выведем значения элементов в виде обычных дробей (если дробь отрицательная, возьмем ее в скобки)
  print('elem =', '(-1) **', n, '* 1/' + str(2 ** n) + ') =', elem_string_brac)
  # наполним список значениями elem
  elem_list.append(elem)
  summ += elem
  # print('сумма:', summ)
print()

elem_list_summ_string = ''
sign = ''
for index, element in enumerate(elem_list):
  if (index != 0)  and (element >= 0):
    sign = ' + '
  else:
    sign = ' '
    
  if index == 0:
    elem_list_summ_string = str(Fraction(element))
  else:
    elem_list_summ_string = elem_list_summ_string + sign + str(Fraction(element))
    
print('Сумма равна:')
print('s =', elem_list_summ_string, '=', summ)


print()
print('-------------')
print()
print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

a = int(input('Введите число "a": '))    # 1    1    17   17   17   2
b = int(input('Введите число "b": '))    # 15   2    25   25   25   1
c = int(input('Введите число "c": '))    # 3    3    3    4    5    2
total_sum = 0
avarege_number = 0
numbers_count = 0
# поскольку прямо не указано иное, предположим, что "b > a", "a > 0", "b > 0"
if (b > a) and (a > 0) and (b > 0):
  for number in range(a + c - a % c, b + 1, c):
    # print('number =', number)
    total_sum += number
    numbers_count += 1
  if numbers_count != 0:  # исключим деление на ноль и сообщим соотв. информацию, если равно нулю  
    avarege_number = total_sum / numbers_count
    print()
    print('Cреднее арифметическое всех чисел из отрезка [' + str(a) + '; ' + str(b) + ']' + ', кратных числу ' + str(c) + ', равно:', avarege_number)
  else:
    print('Чисел из отрезка [' + str(a) + '; ' + str(b) + ']' + ', кратных числу ' + str(c) + ', не найдено!')
  
else:
  print('Расчет осуществляется только при условии "b > a", "a > 0", "b > 0"!')

print()
print('-------------')
print()
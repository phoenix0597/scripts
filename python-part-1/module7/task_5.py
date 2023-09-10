print('Задача 5. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

# (среднее арифметическое можно посчитать поделив сумму подходящих чисел на их количество)

begin_point = int(input('Введите начальную точку (число): '))
end_point = int(input('Введите конечную точку (число): '))
sum_num_multiple3, num_multiple3, avarege_num = 0, 0, 0
for count in range(begin_point, end_point + 1):
  if count % 3 == 0:
    sum_num_multiple3 += count
    num_multiple3 += 1

avarege_num = sum_num_multiple3 / num_multiple3
print('Cреднее арифметическое всех чисел из указанного диапазона, которые кратны числу 3:', avarege_num)

print()
print('-------------')
print()
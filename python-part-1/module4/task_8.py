print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно 

num_1 = int(input('Введите первое число: '))
max_num = num_1
num_2 = int(input('Введите второе число: '))
if max_num < num_2:
  max_num = num_2
num_3 = int(input('Введите третье число: '))
if max_num < num_3:
  max_num = num_3

print('Максимальное из введенных чисел:', max_num)

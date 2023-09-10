print('Задача 8. Яма ')

# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:

# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

size = int(input('Введите высоту фигуры: '))
print()

for row in range(1, size + 1):
  for col1 in range(1, size + 1):
    if (col1 <= row):
      print(size + 1 - col1, end = '')
    else:
      print('.', end = '')
  for col2 in range(size + 1, size * 2 + 1):
    if (col2 > size * 2 - row):
      print(col2 - size, end = '')    
    else:
      print('.', end = '')
  print()
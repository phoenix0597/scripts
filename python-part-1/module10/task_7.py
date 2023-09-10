print('Задача 7. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

rows = int(input('Введите высоту пирамиды: '))
columns = rows * 2
middle = rows - 1
odd_number = 1
print()
for row in range(rows):
  for col in range(columns + 1):
    if (col + row > middle - 1) and (col - row < middle + 1) and (col + row + middle) % 2 == 0:
      print(odd_number, end = '\t')
      odd_number += 2
    else:
      print('\t', end = '')
 
  print()



print('\n--------\n')
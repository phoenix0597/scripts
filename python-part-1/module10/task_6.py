print('Задача 6. Пирамидка')


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######


height = int(input('Введите высоту пирамидки: '))
width = height * 2 - 1
print()
for y in range(height):
  for x in range(width):
    if (x + y < height - 1):
      print(' ', end = '')
    elif (x - y < height):
      print('#', end = '')      
  print()







print('\n--------\n')
print('Задача 1. Калькулятор опыта')

# В свободное время Вася любит играть в компьютерные игры. Однажды у него появилась классная идея для сюжета игры. Чтобы воплотить её в жизнь, он начал изучать геймдизайн. Создавать игру он начал с главного героя и его системы прокачки.

# Напишите программу, которая определяет уровень персонажа в компьютерной игре. Пользователь вводит число «очков опыта», а программа вычисляет уровень. Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта». Начальный уровень равен единице.

# Пример:
# Введите количество опыта: 6000
# Ваш уровень: 4

# Пример 2:
# Введите количество опыта: 2000
# Ваш уровень: 2


exp_score = int(input('Введите количество опыта: '))
points_level_1, points_level_2, points_level_3 = 1000, 2500, 5000
level = 1
if exp_score >= points_level_1:
  if exp_score < points_level_2:
    level = 2
  elif exp_score < points_level_3:
    level = 3
  else:
    level = 4
  
print('Ваш уровень:', level) 
print() 
print('-------------------') 
print() 
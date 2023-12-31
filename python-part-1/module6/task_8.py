print('Задача 8. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.
 
# Напишите программу, 
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
 
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# Подсказка: используйте бинарный поиск, а не конкатенацию.

# пусть мальчик загадал 65
left_border = 0
right_border = 100
attempts = 0
while True:
  middle = left_border + ((right_border - left_border) / 2) // 1
  number = int(input('Твое число равно, меньше или больше, чем число ' + str(middle) + '?\n(1 - равно, 2 - больше, 3 - меньше): ')) # 2 3
  attempts += 1
  if number == 2: # загаданное число больше названного компьютером
    left_border = middle # 50
  elif number == 3: # загаданное число меньше названного компьютером
    right_border = middle # 75
  elif number == 1: # загаданное число равно названному компьютером
    print()
    print('Ты угадал, поздравляю! Число попыток:', attempts)
    break


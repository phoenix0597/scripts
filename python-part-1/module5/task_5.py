print('Задача 5. Вася хочет выигрывать')

# Вася вдохновился фильмом «Двадцать одно» и решил изучить математику игровых автоматов. Для анализа данных ему нужна информация о том, как часто в автомате выпадает три или две одинаковых картинки. Для сбора данных нужна программа, проверяющая это равенство. 

# Даны три целых числа. Определите, сколько среди них совпадающих. 
# Программа должна вывести один из вариантов: 
# 1) 3 (если все совпадают) 
# 2) 2 (если два совпадают)
# 3) 0 (если все числа разные)

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))
matched, num_text = 0, 'чисел'
if (num_1 == num_2) or (num_2 == num_3) or (num_1 == num_3):
  num_text = 'числа'
  matched = 2
  if (num_1 == num_2) and (num_2 == num_3) and (num_1 == num_3):
    matched = 3

print('Совпало', matched, num_text)

print() 
print('-------------------') 
print() 
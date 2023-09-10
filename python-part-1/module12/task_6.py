print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def largestDivisor(a, b):
  min_num = int(((a + b) - abs(a - b)) / 2)
  max_num = int(((a + b) + abs(a - b)) / 2)
  div = 1
  if max_num % min_num == 0:
    div = min_num
  else:
    for i in range(min_num, 1, -1):
      if (min_num % i == 0) and (max_num % i == 0):
        div = i
        break
    
  print('\nНаибольшим общим делителем для чисел', a, 'и', b, 'является', div)


num_1 = int(input('Введите 1-е целое положительное число '))
num_2 = int(input('Введите 2-е целое положительное число '))

largestDivisor(num_1, num_2)


print('\n--------\n')
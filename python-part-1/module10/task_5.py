print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

numCount = int(input('Введите количество чисел: '))
summ, sumMax, numCurrent, numMax = 0, 0, 0, 0

for num in range(1, numCount + 1):
  print('Введите ' + str(num) + '-е натуральное число: ', end = '')
  number = int(input())
  numCurrent = number
  summ = 0
  while numCurrent > 0:
    summ += numCurrent % 10
    numCurrent //= 10
    if summ > sumMax:
      sumMax = summ
      numMax = number
      # print('sumMax =', sumMax, 'numMax =', numMax)
    
print('\nНаибольшее по сумме цифр число:', numMax, '\nCумма его цифр равняется:', sumMax)    



print('\n--------\n')
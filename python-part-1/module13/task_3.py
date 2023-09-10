print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225


def reverse_number(num):
  reversedString = ''
  numAsString = str(num)
  charCount = len(numAsString)

  if num == 0:
    print('Программа завершена!')
  else:
    while charCount > 0:
      charCount -= 1
      reversedString += numAsString[charCount]
      
  return int(reversedString)
  
# Основная программа
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
print('\nПервое число наоборот:', reverse_number(num_1))
print('Второе число наоборот:', reverse_number(num_2))

summReversedNumbers = reverse_number(num_1) + reverse_number(num_2)
print('\nСумма:', summReversedNumbers)
print('Сумма наоборот:', reverse_number(summReversedNumbers))

print('\n--------\n')
  
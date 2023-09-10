print('Задача 4. Число наоборот')

# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321
# 
# Введите число: 1000
# Число наоборот: 0001
# 
# Введите число: 0
# Программа завершена!
# 
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.
# 
# Введите число: 1230
# Число наоборот: 321
# 
# Кстати, нули, которые мы убрали, называются ведущими.

def reverseString(number):
  reversedString = ''
  string = str(number)
  charCount = len(string)

  if number == 0:
    print('Программа завершена!')
  else:
    while charCount > 0:
      charCount -= 1
      reversedString += string[charCount]
  
    if reversedString[0] == '0':
      if int(input('Убирать ведущие нули? \n("убирать" - 1, "не убирать" - любое другие число): ')) == 1:
        reversedNumber = int(reversedString)
      else:
        reversedNumber = str(reversedString)
    else:
      reversedNumber = str(reversedString)
      
    print('Число наоборот:', reversedNumber)
  
# Основная программа
number = int(input('Введите число: '))
reverseString(number)

print('\n--------\n')
print('Задача 8. Поменять местами: не всё так просто! (необязательная, повышенной сложности)')

# Вы уже умеете менять местами строковые переменные и знаете, 
# что в переменных кроме строк можно хранить и числа. 
# Напишите программу, которая меняла бы значения двух переменных местами, 
# но без использования третьей переменной и синтаксического сахара, который мы разбирали, а именно: 
# без конструкции a, b = b, a. В переменные будут вводиться только числа.

a = int(input('Введите первое число: '))            # 11
b = int(input('Введите второе число: '))            # 22
print(a, b)                                         # 11 22

a = a + b                                           # 11 + 22 == 33
b = a - b                                           # 33 - 22 == 11
a = a - b                                           # 33 - 11 == 22

print(a, b)                                          # 22 11

# Не изменяйте уже написанный код (input-ы и print-ы). Между принтами можно вставить столько строк кода, сколько вам нужно для решения.
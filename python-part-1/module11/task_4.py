print('Задача 4. Первая цифра')

# Дано положительное действительное число X. 
# Выведите его первую цифру после десятичной точки. 
# При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками

num = float(input('Введите число: '))
print('\nВ числе',  num, '1-й цифрой после десятичной точки является цифра', int(num % 1 * 10 // 1))







print('\n--------\n')
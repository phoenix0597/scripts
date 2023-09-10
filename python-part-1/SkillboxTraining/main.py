max_danger = float(input('Введите допустимый уровень опасности: '))

if max_danger < 0:
    print('Вы ввели недопустимое значение! Попробуйте еще раз.')
else:
    d_min = 0
    d_max = 4
    d_middle = (d_min + d_max) / 2
    middle_danger = d_middle ** 3 - 3 * d_middle ** 2 - 12 * d_middle + 10
    while abs(middle_danger) > max_danger:
        if middle_danger > 0:
            d_min = d_middle
        else:
            d_max = d_middle
        d_middle = (d_min + d_max) / 2
        middle_danger = d_middle ** 3 - 3 * d_middle ** 2 - 12 * d_middle + 10
    print('Приблизительная глубина безопасной кладки:', d_middle, 'м')


# max_danger = float(input('Введите максимально допустимый уровень опасности: '))
# depth, danger = 0, max_danger + 1
# step = 1e-6

# while danger > max_danger:
#     depth += step
#     if depth > 4:
#         break
#     danger = depth**3 - 3 * (depth**2) - 12 * depth + 10

# print('Приблизительная глубина безопасной кладки:', depth, 'м')


# Решение кубического уравнения
# https://www.webmath.ru/web/prog19_1.php


# def count_number_len(x):
#     count = 0
#     while x:
#         count += 1
#         x //= 10
#         return count

# x = 1234
# print(count_number_len(x))

# def check_number(number):
#     return count_number_len(number) > 4

# def count_number_len(x):
#     count = 0
#     while x is not None:
#         count += 1
#         x //= 10
#         return count

# x = 1234
# if check_number(x):
#     print("1")
# else:
#     print("2")



# print(0.1 + 0.1 + 0.1)

# n = int(input("Количество чисел в последовательности: "))
# cipher_count = 0
# for i in range(n):
#     new_number = int(input("Введите число: "))
#     while new_number:
#         if new_number % 10 > 5:
#             cipher_count += 1
#         new_number //= 10
# else:
#     print(cipher_count)


# x, y = 0, 0

# for i in range(5):
#     for j in range(10):
#         y += 1
#     x += 1

# print(x, y)



# print("0550" == 550)

# i = 99
# for i in range(1, 10, -2):
#   i += 1
#   print(i)
# print()
# print(i)


# i = 99
# for i in range(1, 10, 2):
#   i += 1
#   print(i)

# print('\n', i)



# x = 0
# while x <= 10:
#   x += 1

# print(x)


# x = 0
# if x:
#     x = 1
# print(x == 1)


# x = 100

# if x == 99 and x / 0 == 0:
#     print("hello")


# height = 170
# weight = 70
# lose_weight = True

# if height >= 170 or weight >= 100 and lose_weight == True:
#     print(2000)
# elif height < 170 or weight < 100:
#     print(2500)
# else:
#     print(1800)



# import math

# print(math.sqrt(1.1111111111 ** 3))
# print(math.acos(-6.537037037037037 / 1.1712139481929427))

# for x_10 in range(1, int(4e9)):
#   x = math.log10(x_10)
#   if 0 < x < 4:
#     print('x =', x)

# print(math.log10(int(1)))


# # Задача 2. Сравнение
# def eqv(num_1, num_2, summ):
#   if (num_1 + num_2) - summ < 1e-15:
#     print(True)
#   else:
#     print(False)

# num_1 = float(input('Введите 1-е число: '))
# num_2 = float(input('Введите 2-е число: '))
# summ = float(input('Введите 3-е число: '))
# print('num_1 + num_2 =', num_1 + num_2)
# print('summ =', summ)
# eqv(num_1, num_2, summ)


# # Задача 1. Опять налоги
# def tax(budget, income):
#   print('1e-2 =', 1e-2)
#   if abs(budget + income) - budget > 1e-2:
#     print('Бюджет увеличился')
#   else:
#     print('Бюджет не изменится')


# budget = float(input('Введите бюджет страны: '))
# income = float(input('Новые поступления: '))
# tax(budget, income)


# # Максимальное и минимальное числа в Python
# # Задание точности. Понятие числа Эпсилон машинное
# maxNum = 1.7976931348623157e+308
# minNum = 2.2250738585072014e-308
# a = 0.2
# b = 0.2
# epsilonOfMachine = 1e-16
# # Сравнение вещественных чисел производится следующим образом
# if abs(a - b) < 1e-15:
#   print('Только что мы задали точность - 15 знаков после запятой')
#   print('Равно')
# else:
#   print('Не равно')




# # Задача 3. Урок информатики
# def floatPoint(number):
#   if number % 1 != 0 or number < 10:
#     print('Ошибка ввода! Введите положительное целое число больше 10.')
#   else:
#     numberLength = len(str(number))
#     order = numberLength - 1
#     if number % 1 == 0 and number > 10:
#       print('Формат плавающей точки: x =', number / (10 ** order), '*', 10, '**', order)

# number = int(input('Введите целое положительное число больше 10: '))
# floatPoint(number)




# # Задача 2. Тестирование
# numberAsString = input('Введите число в экспоненциальномм формате: ')
# numberAsNumber = float(numberAsString)
# x = 1
# count = 0
# while x <= 2:
#   x += numberAsNumber
#   count += 1

# print('Количество прибавлений:', count)



# # Задача 1. Возможности компьютера
# x = 1
# count = 0
# while x != 0:
#   x /= 2
#   count += 1
#   print(x)
# print('Количество итераций:', count)



# # Задача 3. Приоритет задач
# def numeral_count():
#   numeral = int(input('Введите количество задач: '))
#   firstPriorityTask = 0
#   for i in range(numeral):
#     num = int(input('Введите число: '))
#     if num > firstPriorityTask:
#       firstPriorityTask = num
      
#   return firstPriorityTask

# print('Первая задача на обработку:', numeral_count())



# # Задача 2. «Назад в будущее» (определяем НОД)
# def gcd(num_1, num_2):
#   maxNum = ((num_1 + num_2) + abs(num_1 - num_2)) / 2
#   minNum = ((num_1 + num_2) - abs(num_1 - num_2)) / 2
#   gcd = 1
#   if maxNum % minNum == 0:
#     gcd = minNum
#   else:
#     gcdSearch = minNum
#     while gcdSearch > 0:
#       gcdSearch -= 1
#       if maxNum % gcdSearch == 0 and minNum % gcdSearch == 0:
#         gcd = gcdSearch
#         break
#   return int(gcd)

# num_1 = int(input('Введите 1-е целое положительное число: '))
# num_2 = int(input('Введите 2-е целое положительное число: '))
# print('НОД =', gcd(num_1, num_2))
  




# # Задача 1. Сумма чисел 2
# def summa_n(num):
#   summ_1 = (1 + num) / 2 * num
#   return int(summ_1)

# number = int(input('Введите целое положительное число '))

# print('Сумма от 1 до', number, '=', summa_n(number))
# print('Сумма от 1 до', summa_n(number), '=', summa_n(summa_n(number)))




# print('Задача 6. НОД')

# #Напишите функцию, вычисляющую наибольший общий делитель двух чисел

# def largestDivisor(a, b):
#   min_num = int(((a + b) - abs(a - b)) / 2)
#   max_num = int(((a + b) + abs(a - b)) / 2)
#   div = 1
#   if max_num % min_num == 0:
#     div = min_num
#   else:
#     for i in range(min_num, 1, -1):
#       if (min_num % i == 0) and (max_num % i == 0):
#         div = i
#         break
    
#   print('\nНаибольшим общим делителем для чисел', a, 'и', b, 'является', div)


# num_1 = int(input('Введите 1-е целое положительное число '))
# num_2 = int(input('Введите 2-е целое положительное число '))

# largestDivisor(num_1, num_2)


# print('\n--------\n')


# # Индекс массы тела
# height = float(input('Введите рост (м): '))
# weight = float(input('Введите вес (кг): '))

# bmi = round(weight / height ** 2, 2)
# print('Ваш индекс массы тела', bmi)
# if bmi < 18.5:
#   print('У вас недостаточная масса тела')
# elif bmi <  25:
#   print('У вас нормальная масса тела')
# else:
#   print('У вас ожирение')




# def mainMenu():
#   print('1. Сделать что-то хорошее')
#   print('2. Сделать что-то плохое')
#   choice = int(input('Введите номер действия: '))
#   if choice == 1:
#     good()
#   elif choice == 2:
#     bad()
#   else:
#     print('Ошибка ввода: нужно ввести 1 или 2.')


# def good():
#   print('\nВсе хорошо.')
#   input('Нажмите любую кнопку, чтобы вернуться в меню. \n')
#   mainMenu()

# def bad():
#   print('\nВсе плохо.')
#   mainMenu()
# mainMenu()





# # GPS-навигатор 2
# import math

# def distanceFromZero(x, y):
#   distance = math.sqrt(x ** 2 + y ** 2)
#   print('\nРасстояние до точки назначения:', distance)

# def distanceFromPointToPoint(x_1, y_1, x_2, y_2):
#   distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
#   print('\nРасстояние до точки назначения:', distance)

# print('Нужно найти расстояние от себя до точки (ответ - "1") \nили между двумя произвольными точками (ответ - "2")?')
# answer = int(input(':'))
# if answer == 1:
#   print('\nВведите координаты точки назначения')
#   x = float(input(':'))
#   y = float(input(':'))
#   distanceFromZero(x, y)
# elif answer == 2:
#   print('\nВведите координаты своего местонахождения')
#   x_1 = float(input(':'))
#   y_1 = float(input(':'))
#   print('\nВведите координаты точки назначения')
#   x_2 = float(input(':'))
#   y_2 = float(input(':'))
#   distanceFromPointToPoint(x_1, y_1, x_2, y_2)
# else:
#   print('\nОшибка ввода.')
  


# # Почта 2
# def pesonalData(surname, name, country, town, street, building, apartment):
#   print('Имя:', surname)
#   print('Фамилия:', name)  
#   print('Страна:', country)
#   print('Город:', town)
#   print('Улица:', street)
#   print('Дом:', building)
#   print('Квартира:', apartment, '\n')
    
# pesonalData('Эльдар', 'Рязанов', 'Россия', 'Москва', 'Пушкина', '34', '14')
# pesonalData('Евгений', 'Мягков', 'Россия', 'Ленинград', 'Строителей', '32', '25')
# pesonalData('Барбара', 'Брыльска', 'Россия', 'Москва', 'Строителей', '32', '25')



# def averageOfNumbersRange(a, b):
#   print('\nСреднее арифметическое всех чисел из отрезка [' + str(a) + '; '+ str(b) +']:', (a + b) / 2)

# left_border = int(input('Введите левую границу: '))
# right_border = int(input('Введите правую границу: '))
# if right_border > left_border:
#   averageOfNumbersRange(left_border, right_border)
# else:
#   print('\nОшибка ввода, первое число должно быть меньше второго')


# # Проверка числа на простоту
# def isPrime(num):
#   theNumIsPrime = True
#   for n in range(2, num):
#     if num / n == num // n:
#       theNumIsPrime = False
#   return theNumIsPrime

# numbersCount = int(input('Введите количество чисел для проверки: '))
# isPrimeCount = 0
# for num in range(numbersCount):
#   print('Введите число ' + str(num + 1) + ': ', end = '')
#   number = int(input())
#   if isPrime(number):
#     isPrimeCount += 1
# print('\nКоличество простых чисел в приведенной последовательности:', isPrimeCount)
  


# # Вот это объёмы 2
# import math

# def sphereArea(radius):
#   print('\nПлощадь сферы с данным радиусом составляет S =', 4 * math.pi * radius ** 2)

# def sphereVolume(radius):
#     print('\nОбъем сферы с данным радиусом составляет V =', 4 / 3 * math.pi * radius ** 3)  

# radius = float(input('Введите радиус: '))
# sphereArea(radius)
# sphereVolume(radius)

# # Вода
# def aboutWater(price):
#   print('Название: КлирВотер')
#   print('Производитель: ВодЗавод')
#   print('Цена:', price, '\n')

# aboutWater(25)
# aboutWater(30)
# aboutWater(40)




# # Использование функции для математических расчетов
# import math

# def func(x):
#   if -5 <= x <= 5:
#     print('x =', x, 'y =', math.exp(x))
#   elif x < -5:
#     print('x =', x, 'y =', 2 * abs(x) - 1)
#   else:
#     print('x =', x, 'y =', 2 * x)

# for x in range(-10, 11):
#   func(x)


# # Почта
# name = ''
# surname = ''
# street = ''
# build =  '0'


# def pesonalData(name, surname, street, build):
#   print('Фамилия:', name)
#   print('Имя:', surname)
#   print('Улица:', street)
#   print('Дом:', build, '\n')
  
# pesonalData('Василий', 'Иванов', 'Пушкина', '32')
# pesonalData('Игорь', 'Иванов', 'Пушкина', '32')
# pesonalData('Алена', 'Иванов', 'Пушкина', '32')


# # Провизия
# def countAllBags():
#   a = int(input(': '))
#   b = int(input(': '))
#   print("Всего", a + b, "шт.\n")


# print("Сколько мешков рыбы и мяса?")
# countAllBags()

# print("Сколько буханок белого и чёрного хлеба?")
# countAllBags()

# print("Сколько вёдер воды и молока?")
# countAllBags()



# # Робот-швейцар
# def greeting():
#   print('Привет!')
#   print('Добро пожаловать!')
 

# while True:
#   answer = input('Зайдёте? Да/Нет: ')
#   if answer == 'Да':
#     greeting()
#   print('Следующий.\n')



# # Функции треугольник и прямоугольник
# def triangle():
#   stars = 1
#   for line in range(5):
#     print(' ' * (5 - line - 1), end = '')
#     print('*' * stars)
#     stars += 2

# def rectangle():
#   stars = 1
#   for line in range(5):
#     if line == 0 or line == 4:
#       print('*' * 5)
#     else:
#       print('*' + ' ' * 3 + '*')
#     stars += 2

# choice  = int(input('Что рисуем? 1 - треугольник, 2- прямоугольник: '))
# if choice == 1:
#   triangle()
# elif choice == 2:
#   rectangle()
# else:
#   print('Ошибка ввода')


# # Найти большее число, не прибегая к помощи условных операторов и циклов
# num_1 = float(input('Введите первое число: '))
# num_2 = float(input('Введите второе число: '))

# maxNum = ( (num_1 + num_2) + abs(num_1 - num_2)) / 2
# print('\nНаибольшее число:', int(maxNum))



# summ = 1.1 + 2.2
# print('summ =', summ)
# if round(summ, 1) == 3.3:
#   print('Сумма равна')
# else:
#   print('Сумма не равна')


# # Мега-калькулятор
# import math

# number = float(input('Введите число для вычисления различных функций: '))

# roundedToLess = math.floor(number)
# roundedToMore = math.ceil(number)
# module = abs(number)
# squareRoot = math.sqrt(number)
# expToDegree = math.exp(number)
# natLog = math.log(number)
# logTwo = math.log2(number)
# logTen = math.log10(number)
# sinus = math.sin(number / 57.2958)
# cosinos = math.cos(number / 57.2958)

# print('\nЧисло', number, 'округлено в меньшую сторону:', roundedToLess)
# print('\nЧисло', number, 'округлено в меньшую сторону:', roundedToMore)
# print('\nМодуль числа', number, 'равен', module)
# print('\nКвадратный корень из числа', number, 'равен', squareRoot)
# print('\nНатуральный логарифм числа', number, 'равен', natLog)
# print('\nЛогарифм числа', number, 'по основанию 2 равен', logTwo)
# print('\nЛогарифм числа', number, 'по основанию 10 равен', logTen)
# print('\nСинус числа', number, 'равен', sinus)
# print('\nКосинус числа', number, 'равен', cosinos)


# if number == number // 1:
#   factor = math.factorial(int(number))
#   print('\nФакториал числа', int(number), 'равен', factor)


# # 2D-игра
# import math
# distance = float(input('Какое расстояние пройдено (км)? '))
# angle = float(input('Какое был угол движения относительно севера (азимут) в градусах? '))
# angle /= 57.2958

# x = distance * math.sin(angle)
# y = distance * math.cos(angle)

# print('Координаты нового местоположения игрока:', x, ',', y)



# # Задача 1. Формула Герона (вычисляем площадь треугольника по значениям его сторон)
# import math

# a = float(input('Введите длину 1-й стороны: '))
# b = float(input('Введите длину 2-й стороны: '))
# c = float(input('Введите длину 3-й стороны: '))

# halfPerimetr = (a + b + c) / 2

# area = math.sqrt(halfPerimetr * (halfPerimetr - a) * (halfPerimetr - b) * (halfPerimetr - c))
# print('Площадь треугольника с указанными размерами сторон составляет: ', area)


# # Локатор (вычисление координат вражеского танка)
# import math

# distance = float(input('Введите расстояние до танка: '))
# angle = float(input('Введите угол в градусах: '))

# # получаем угол в радианах для дальнейшей передачи его в тригонометрические функции
# angle /= 57.2958

# x = math.cos(angle) * distance
# y = math.sin(angle) * distance

# print('Координаты вражеского танка:', x, ',', y)



# GPS-навигатор
# import math

# x = int(input('Введите координату x: '))
# y = int(input('Введите координату y: '))

# distance = math.sqrt(x ** 2 + y ** 2)

# print('Расстояние до объекта:', distance)



# # Шахматная доска (0.8 x 0.8 m2)
# x = float(input('Расположение по горизонтали: '))
# y = float(input('Расположение по вертикали: '))

# xSquare = int(x * 10)
# ySquare = int(y * 10)

# xShift = round(xSquare / 10 + 0.05 - x, 3)
# yShift = round(ySquare / 10 + 0.05 - y, 3)

# if xSquare in range(8) and ySquare in range(8):
#   print('\nФигура находится в клетке ('+ str(xSquare) + ', ' + str(ySquare) + ')')
#   if xShift > 0 or yShift > 0:
#     print('\nПоправьте положение фигуры на ('+ str(xShift) + ', ' + str(yShift) + ')')
# else:
#   print('\nКлетки с такой координатой не существует')




# # Удар
# while True:
#   force = float(input('Сила удара: '))
#   force *= 10
#   print('Балл:', int(force))



# # День рождения
# age = int(input('Сколько лет имениннику? '))
# tempr = float(input('Какая температура тела (в градусах по Цельсию)? '))

# gift = round(age * 1.5 * tempr, 2)

# print('Сумма денег для подарка составит:', gift, 'рублей.')




# # Индекс массы тела
# height = float(input('Введите рост (м): '))
# weight = float(input('Введите вес (кг): '))

# bmi = round(weight / height ** 2, 2)
# print('Ваш индекс массы тела', bmi)
# if bmi < 18.5:
#   print('У вас недостаточная масса тела')
# elif bmi <  25:
#   print('У вас нормальная масса тела')
# else:
#   print('У вас ожирение')



# # Ставки на спорт
# bet  = int(input('Сколько ставим? '))
# coef = float(input('Какой коэффициент? '))

# win = round(bet * coef, 2)

# print('Потенциальный выигрыш:', win)
# print(win)


# print('Задача 8. Яма ')

# # Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:

# # Напишите программу,
# # которая получает на вход число N и выводит на экран числа в виде “ямы”:

# # Введите число: 5
# #
# # 5........5
# # 54......45
# # 543....345
# # 5432..2345
# # 5432112345

# size = int(input('Введите высоту фигуры: '))
# print()

# for row in range(1, size + 1):
#   for col1 in range(1, size + 1):
#     if (col1 <= row):
#       print(size + 1 - col1, end = '')
#     else:
#       print('.', end = '')
#   for col2 in range(size + 1, size * 2 + 1):
#     if (col2 > size * 2 - row):
#       print(col2 - size, end = '')    
#     else:
#       print('.', end = '')
#   print()



# print('Задача 7. Метод бутерброда')

# # В секретном агентстве Super-Secret-no решили использовать «метод бутерброда» для шифрования переписки своих сотрудников. Сначала буквы слова нумеруются в таком порядке: первая буква получает номер 1, последняя буква — номер 2, вторая — номер 3, предпоследняя — номер 4, потом третья… и так для всех букв (см. рисунок). Затем все буквы записываются в шифр в порядке своих номеров.

# # Например, слово «sandwich» зашифруется в «shacnidw».
# # К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# # И теперь агенты не могут понять, что же они написали друг другу. Помогите им.

# # Пример:
# # Введите зашифрованное сообщение: shacnidw
# # Расшифрованное сообщение: sandwich
# #          1   3   5   7   8   6   4   2
# # Слово: | s | a | n | d | w | i | c | h |
# # Шифр:  | s | h | a | c | n | i | d | w |


# word = input('Введите зашифрованное слово: ')
# sum_1 = ''
# sum_2 = ''
# count = 0
# for letter in word:
#     count += 1
#     if count % 2 != 0:
#         sum_1 += letter
#     else:
#         sum_2 = letter + sum_2
# print('Расшифрованное слово: ', sum_1 + sum_2)



# while True:
#   for attempt in range(1, 4):
#     pincode = int(input('Введите пинкод: '))
#     if pincode == 1234:
#       print('\nПин-код верный. Держите вашу зарплату!')
#       break
#     print('\nПин-код неверный. Осталось попыток', 3 - attempt)
#   else:
#     print('\nВаша карта заблокирована. Для возврата карты обратитесь в банк-эмитент.')
#   print('\nСледующий клиент, добро пожаловать')




# # Лестница чисел
# size = int(input('Введите размер полуматрицы: '))
# x, y = 0, 0
# for y in range(size + 1):
#   for x in range(size + 1):
#     if x + y <= size:
#       print(x + y, end = '\t')
#   print('\n')  

# # Цифры больше пяти
# # Пользователь вводит последовательность из N чисел. Напишите программу, которая подсчитывает общее количество цифр больше пяти во всей последовательности.

# numeral = int(input('Введите количество чисел: '))
# searchNum = int(input('Больше какой цифры нужно искать числа? '))
# numeralCount = 0

# for i in range(1, numeral + 1):
#   print('Введите ' + str(i) + '-е число: ', end = '')
#   number = int(input())
#   if number > searchNum:
#     numeralCount += 1
  
# print('\nКоличество чисел, больше ' + str(searchNum) + ': ', numeralCount)      
      
      
  
# number = int(input('Введите количество людей в очереди: '))
# for hour in range(number):
#   print('\n' + str(hour) + '-й час:\n---')
#   for person in range(hour, number):
#     print(str(person) + '-й человек')
# print('\nОчередь обслужена!')




# # Ворота (поле 20 х 50)
# for row in range (20):
#   for col in range(30):
#     if (row == 0):
#       print('-', end = '')
#     elif (col == 0) or (col == 29):
#       print('|', end = '')
#     else:
#       print(' ', end ='')
#   print()



# # Координатные оси (поле 20 х 50)
# for row in range (20):
#   for col in range(50):
#     if row == 9:
#       print('-', end = '')
#     elif col - row == 30:
#       print('\\', end = '')
#     elif col + row == 18:
#       print('/', end = '')
#     elif col == 24:
#       print('|', end = '')
#     else:
#       print(' ', end ='')
#   print()


# # Матрица 3
# size = int(input('Введите размер матрицы: '))
# print()
# for row in range(size):
#   for col in range(size):
#     if row == col:
#       print('1', end = ' ')
#     elif col > row:
#       print('0', end = ' ')
#     else:
#       print('2', end = ' ')
#   print()
      



# # Координатные оси (поле 20 х 50)
# for row in range (20):
#   for col in range(50):
#     if row == 9:
#       print('-', end = '')
#     elif col == 24:
#       print('|', end = '')
#     else:
#       print(' ', end ='')
#   print()

    
   
# # Матрица 2
# number = int(input('Введите размер матрицы: '))
# for row in range(1, number + 1):
#   for col in range(1, number + 1):
#     if col % 3 == 0:
#       print(col, end = ' ')
#     else:
#       print(row, end = ' ')
#   print()
# print('\n-------------\n')



# # Матрица
# number = int(input('Введите размер матрицы: '))
# for row in range(1, number + 1):
#   for col in range(1, number + 1):
#     if row % 2 == 0:
#       print(row, end = ' ')
#     else:
#       print(col, end = ' ')
#   print()
# print('\n-------------\n')



# # Таблица сложения 2
# for a in range(10):
#   for b in range(0, -10, -1):
#     print(a + b, end = '\t')
#   print()
# print('\n-------------\n')

# # Таблица сложения
# number = int(input('Введите число: '))
# for a in range(number):
#   for b in range(number):
#     print(a + b, end = '\t')
#   print()
# print('\n-------------\n')


# # Таблица умножения
# for a in range(1, 10):
#   for b in range(1, 10):
#     print(a * b, end = '\t')
#   print()



# # поиск двух одинаковых букв подряд
# string = input('Введите строку: ')
# prevSym = ''
# equalSym = False
# for letter in string:
#   if letter == prevSym:
#     equalSym = True
#     break
#   else:
#     prevSym = letter
# if equalSym == True:
#   print('Есть две одинаковые буквы подряд')
# else:
#   print('Нет двух одинаковых букв подряд')
  


# # Отфильтрованный текст
# text = input('Введите текст: ')
# summ = 0
# print('\nОтфильтрованный текст: ', end = ' ')
# for symbol in text:
#   if symbol == '1' or symbol == '9':
#     summ += int(symbol)
#   else:
#     print(symbol, end = '')
# print('\nСумма:', summ)




# # Задача 3. Табло
# number = int(input('Введите число: '))

# print('-=-', end = ' ')
# for num in range(0, number +1, 10):
#   print(num, end = ' -=- ')
# print()

# # Задача 1. Доска
# for i in range(6):
#   if (i != 0) and (i != 5):
#     print('|' + 'O' * 8 + '|')
#   else:
#     print('-' * 10) # на 0-й и на 6-строке выведем 8 сплошных дефисов


# # Задача 2. Локальная сеть (формирование IP-адреса)
# number = int(input('Введите первое число: ')) # 5
# step = int(input('Введите шаг: ')) # 3
# summ = 0

# print('\nIP-адрес:', end = ' ')
# for count in range(3):
#   print(number, end ='.')
#   summ += number
#   number += step
# print(summ)  # 5.8.11.24



# phrase = input('Введите фразу: ' )
# for symbol in phrase:
#   print(symbol, end = '1 ')



# text = input('Введите текст: ') # Прыг скок
# big_y, big_y_count = 'Ы', 0
# small_y, small_y_count = 'ы', 0

# for symbol in text:
#   if symbol == big_y:
#     big_y_count += 1
#   if symbol == small_y:
#     small_y_count += 1

# print('Больших букв Ы: ', big_y_count)
# print('Маленьких букв Ы: ', small_y_count)
  


# text = input('Введите текст: ')
# first_sym = input('Введите первую букву: ')
# second_sym = input('Введите вторую букву: ')
# firstSymCount = 0
# secondSymCount = 0

# for symbol in text:
#   if symbol == first_sym:
#     firstSymCount += 1
#   if symbol == second_sym:
#     secondSymCount += 1

# print('Кол-во букв: ' + first_sym + ' = ' + str(firstSymCount) + '; ' + second_sym + ' = ' + str(secondSymCount))
  


# phrase = input('Введите фразу: ' )
# for symbol in phrase:
#   print(symbol * 5)
#   print('=' * 10)



# # сравнение строк 2
# right_answer = 'Да, конечно, сделал'
# while 1:
#   answer = input('Василий, сделал ли ты вчерашнее задание? ')
#   if answer == 'Да, конечно, сделал':
#     break

# # сравнение строк 2
# username = input('Как тебя зовут? ')
# answer = input(username + ', ' +'купи слона! ')
# while 1:
#   answer = input('Все говорят ' + answer + ' а ты купи слона! ')



# # сравнение строк 1
# badGradeCount = 0
# for student in range(5):
#   answer = input('Кто написал произведение "Евгений Онегин"? ')
#   if (answer == 'Пушкин') or (answer == 'пушкин'):
#     print('Верно!')
#     break
#   print('Неправильно! Два!')
#   badGradeCount += 1
# print('Кол-во двоек: ', badGradeCount)




# # Прятки (усложнение)
# seconds = int(input('Введите количество секунд для счета: '))
# for sec in range(seconds, 0, -2):
#   print(sec)
# print('Я иду искать!')


# # Армия (усложнение)
# totalSoldiers = int(input('Количество солдат в шеренге: '))
# totalrules = int(input('Количество правил в уставе: '))
# pushups_count = 0
# for soldier in range(totalSoldiers-3, 0, -4):
#   answer = int(input('Солдат, назови количество правил в уставе? '))
#   if answer != totalrules:
#     print('Неправильно!', 10 * soldier, 'отжиманий!')
#     pushups_count += 10 * soldier
#   else:
#     print('Молодец, правильно!')
# print('Всего отжались раз:', pushups_count)


# # Прятки
# seconds = int(input('Введите количество секунд для счета: '))
# for sec in range(seconds, 0, -1):
#   print(sec)
# print('Я иду искать!')

# # Армия
# totalSoldiers = int(input('Количество солдат в шеренге: '))
# totalrules = int(input('Количество правил в уставе: '))
# pushups_count = 0
# for soldier in range(totalSoldiers, 0, -4):
#   answer = int(input('Солдат, назови количество правил в уставе? '))
#   if answer != totalrules:
#     print('Неправильно!', 10 * soldier, 'отжиманий!')
#     pushups_count += 10 * soldier
#   else:
#     print('Молодец, правильно!')
# print('Всего отжались раз:', pushups_count)

# seconds = int(input('Введите количество секунд: '))
# for sec in range(seconds, -1, -1):
#   print('Микроволновка греет', sec, 'секунд.')
# print('Дзинь!')

# # Диета
# wake_up = int(input('Во сколько проснулись? '))
# calories = 0
# water = 0
# for hour in range(wake_up, 23, 3):
#   calories += int(input('Сколько съели калорий? '))
#   water += 1
# print('Вы съели ', calories, 'калорий и выпили', water, 'л воды.')


# # Театр
# last_number = int(input('Введите номер последнего стула: '))
# numbers_sum = 0
# for current in range(1, last_number + 1, 5):
#   print('Номер стула:', current)
#   numbers_sum += current
# print('Сумма:', numbers_sum)


# # Кубы нечётных чисел
# number = int(input('Введите число: '))
# for num in range(1, number + 1, 2):
#   print(num, '** 3 =', num  ** 3)


# # Квадраты нечётных чисел
# number = int(input('Введите число: '))
# for num in range(1, number // 2 + number % 2 + 1):
#   print(num * 2 - 1, '** 2 =', (num * 2 - 1) ** 2)


# # Деление клетки
# totalHours = int(input('Сколько часов будем наблюдать? '))
# cells_count = 1
# for hour in range(1, totalHours // 3 + 1):
#   cells_count *= 2
#   print()
#   print('Прошло часов:', hour * 3)
#   print('Клеток:', cells_count)
#   print('Часов до конца эксперимента:', totalHours - hour * 3)



# # Таблица кубов
# number = int(input('Введите число: '))
# for current_num in range(number // 2 + 1):
#   print(current_num * 2, '** 3 =', (current_num * 2) ** 3)



# # вывести элементы списка без скобок
# print(*list(range(1, 5)), sep = ', ')
# print(*list(range(1, 5)))
# import this


# # Поел — можно и поспать, поспал — можно и поесть
# total_calories = 0
# total_no_sleep = 0
# for hour in range(0, 23):
#   print('Час', hour + 1)
#   calories = int(input('Сколько съел калорий? '))
#   total_calories += calories
#   if total_calories >= 2000:
#     break
#   total_no_sleep += 1
# print('Всего бодрствовал:', total_no_sleep, ' часов. Съел калорий:', total_calories)


# # Сумма чисел
# start_num = int(input('Введите начальную цифру диапазона: '))
# stop_num = int(input('Введите конечную цифру диапазона: '))
# summ = 0
# for num in range(start_num, stop_num + 1):
#   summ += num
# print('Сумма чисел в заданном диапазоне:', summ)
  


# # Квадраты превратились в кубы
# for number in range(1, 11):
#   print(number ** 3)

# # степени числа 2 от 0 до 20
# for degree in range (20):
#   print('Число 2 в степени', degree, 'будет:', 2 ** degree)


# # кукушка
# current_hour = int(input('Который час? '))
# for hour in range(current_hour):
#   print('Ку-ку! (' + str(hour + 1) + ')')


# # квадраты чисел
# for num in range(11):
#   print(num ** 2)


# text = 'Python!'
# for word_count in range(5):
#   print(word_count)
#   print(text)


# for num in 3, 7, 5, 6, 4:
#   print(num ** 2, num ** 3, num ** 4)


# for meters in 100, 90, 95, 87, 102:
#  if meters % 3 == 0:
#    print(meters, 'Подходит')
#  else:
#    print(meters, 'Не подходит')


# winners = 0
# for ticket in 345, 19, 87, 1020, 421, 555:
#   if (ticket % 5 == 0) and (ticket / 100 > 0) and (ticket / 100 < 10):
#     print('Билет', ticket, 'выиграл!')
#     winners += 1
# if winners > 1:
#   winners_text = 'Поздравляем победителей!'
# elif winners == 1:
#   winners_text = 'Поздравляем победителя!'
# else:
#   winners_text = 'К сожалению, в этом розыгрыше никто не выиграл.'
# print('Игра завершена!', winners_text, 'Их количество:', winners)

# for number in 2, 7, 5, 3, 10:
#   print(number ** 2)
  
# left_border = 0
# right_border = 100
# attempts = 0
# while True:
#   middle = left_border + ((right_border - left_border) / 2) // 1
#   number = int(input('Твое число равно, меньше или больше, чем число ' + str(middle) + '?\n(1 - равно, 2 - больше, 3 - меньше): ')) # 2 3
#   attempts += 1
#   if number == 2: # загаданное число больше названного компьютером
#     left_border = middle # 50
#   elif number == 3: # загаданное число меньше названного компьютером
#     right_border = middle # 75
#   elif number == 1: # загаданное число равно названному компьютером
#     print()
#     print('Ты угадал, поздравляю! Число попыток:', attempts)
#     break



# number = int(input('Введите число: '))
# while number > 0:
#   if number == 3:
#     number -= 1
#     continue
#   print(number)
#   number -= 1
    


# bags_count = int(input('Сколько мешков? '))
# counter = 0
# allbags_weight = 0
# while counter < bags_count:
#   bag_weight = int(input('Введите вес '+ str(counter + 1) + '-го мешка в кг: ' ))
#   allbags_weight += bag_weight
#   counter += 1
# print('Перенесено мешков: ' + str(counter) + ', общим весом', allbags_weight, 'кг')



# reminder = 'Вы хотели не забыть кое-что сделать'
# count = int(input('Сколько раз напомнить? '))
# counter = 0
# while counter < count:
#   print(reminder + ' (' + str(counter + 1) + ')')
#   counter += 1


# message = 'Я - программист!'
# count = int(input('Сколько раз повторить вывод текста? '))
# counter = 0
# while counter < count:
#   print(message + ' (' + str(counter + 1) + ')')
#   counter += 1


# code = ''
# while code != '0550':
#   print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
#   code = input('Введите код: ')
# print('Код верный, завершаю работу...')

# count = 10
# while count <= 10:
#  if count == 0:
#    print('Время вышло!')
#    break
#  else:
#    print(count)
#    count -= 1



# while True:
#   active = int(input('Продолжаем работать? 1/0: '))
#   if active ==0:
#     print('Приложение закрывается...')
#     break
# rate = int(input('Поставите оценку приложению? 1/0: '))
# rate_check = (rate == 1)
# print('Работа завершена')
# if rate_check:
#   print('Пользователь поставит оценку')




# wallet_sum = int(input('Сколько всего денег? '))
# while wallet_sum < 10000:
#   number = int(input('Сколько выпало на кубике (от 1 до 6)? '))
#   if number == 3:
#     wallet_sum = 0
#     print('Вы проиграли всё!')
#     break
#   else:
#     print('Выиграли 500 рублей!')
#     wallet_sum += 500
# print('Игра закончена.')
# print('Итого осталось:', wallet_sum, 'рублей')


# в приложернии ____ приведен код, который не выводет часть текста, в случае выигрыша не выведет на экран консоли текст "Выиграли 500 рублей!", а именно:

# start_money = int(input("Введите стартовую сумму: "))
# while start_money < 10000:
#     random_cube = int(input("Сколько выпало на кубике? "))
#     if random_cube == 3:
#         print("Вы проиграли всё!")
#         start_money = 0
#         break
#     print('Выиграли 500 рублей!')  
#     start_money += 500

# print("Игра закончена.\nИтого осталось:", start_money)

# нужно добавить 


# number = int(input('Введите число: '))
# summ = 0
# while number !=0:
#   last_number = number % 10
#   print(last_number)
#   if last_number == 5:
#     print('Обнаружен разрыв!')
#     break
#   summ += last_number
#   number //= 10
# print('Сумма цифр: ', summ)


# temperature = int(input('Сколько градусов на улице? '))
# distance = 0
# while temperature > 15:
#   distance +=20
#   temperature -= 2
#   if temperature <= 15:
#     break
#   distance += 10
# print('Пройдено метров:', distance)


# contribution = int(input('Сколько денег отложить? '))
# savings = contribution
# while savings < 500000:
#   contribution = int(input('Сколько еще денег отложить? '))
#   savings += contribution
# print('Поздравляем, вы накопили более 500000, а именно', savings)




# number = int(input('Введите число: '))
# numbers_sum = 0
# while number != 0:
#  numbers_sum += number
#  number = int(input('Введите число: '))
# print('Сумма введенных чисел равна', numbers_sum)




# balance = int(input('Сколько денег поступило? '))
# while balance > 5000:
#   product_cost = int(input('Введите стоимость товара: '))
#   balance -= product_cost
# print('Внимание! На карте осталось мало денег! Остановитесь!')
# print('Баланс счета:', balance)



# password = int(input('Введите пароль: '))
# while password != 235:
#   print('Неверный пароль')
#   password = int(input('Попробуйте еще раз: '))
# print('Пароль верный. Добро пожаловать!')




# year = int(input('Введите год: '))
# not_part = ' не '
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#   not_part = ' '
  
# print('Год' + not_part + 'является високосным!')



# temperature = int(input('Введите текущую температуру: '))
# if temperature < 0 or temperature > 100:
#   print('Внимание, ваши бактерии подвергаются опасности! Температура вышла из допустимого диапазона!')
# else:
#   print('Температура среды, в которой находятся бактерии, в пределах допустимого диапазона.')



# print('Задача: Определяем поступление в ВУЗ')
# exam_score = int(input('Сколько баллов набрал? '))
# medal_number = int(input('Есть золотая медаль (да - любое количество, нет - 0)? '))
# if exam_score > 280 and medal_number > 0:
#   print('Поздравляем! Ты поступил!')
# else:
#   print('К сожалению, ты не прошел в наш университет.')



# x = int(input('Введите точку икс: '))
# left_border = int(input('Введите левую границу: '))
# right_border = int(input('Введите левую границу: '))
# if x >= left_border and x<= right_border:
#   print('Точка х входит в диапазон')
# else:
#   print('Ошибка: икс вышел за границы диапазона')


# print('Задача: Выбираем велосипед')
# year = int(input('Введите год выпуска: '))
# speed_count = int(input('Введите количество скоростей: '))
# if year < 2018 or speed_count < 24:
#   print('Не соответствует критериям')
# else:
#   print('Подходит!')
  

# coin_weight_1 = int(input('Введите вес первой монеты: '))
# coin_weight_2 = int(input('Введите вес второй монеты: '))
# coin_weight_3 = int(input('Введите вес третьей монеты: '))
# false_coin = 'первая'

# if coin_weight_1 == coin_weight_2:
#   false_coin = 'третья'
# elif coin_weight_1 == coin_weight_3:
#   false_coin = 'вторая'

# print('Фальшивой является', false_coin, 'монета')




# income = int(input('Введите размер дохода: '))
# if income < 10000:
#   tax = income * 13 / 100
#   tax_des = '13%'
# elif income < 50000:
#   tax = income * 20 / 100
#   tax_des = '20%'
# elif income >= 50000:
#   tax = income * 30 / 100
#   tax_des = '30%'
# print('Размер налога (' + tax_des + ') составляет', tax)


# x = int(input('Введите икс: '))
# y = int(input('Введите игрек: '))
# sign = 'больше'
# if x < y:
#   sign = 'меньше'
# elif x == y:
#     sign = 'равно'
# print('X', sign, 'Y')


# cheese_cost = 60
# ice_cream_cost = 20
# money_amount = int(input('Введите количество денег: '))
# if money_amount >= cheese_cost:
#   money_amount -= cheese_cost
#   # print('money_amount =', money_amount)
#   print('На сыр денег хватило')
#   if money_amount >= ice_cream_cost:
#     money_amount -= ice_cream_cost
#     print('И на мороженое тоже!')
#   else:
#       print('Денег на мороженое маловато')

# else: 
#     print('Денег не хватило даже на сыр')
    


# x = int(input('Введите икс: '))
# y = int(input('Введите игрек: '))
# sign = 'больше'
# if x < y:
#   sign = 'меньше'
# if x == y:
#   sign = 'равно'
# print('X', sign, 'Y')



# bank = int(input('Сколько денег на счету? '))
# if bank >= 75000:
#   print('Курс стоимостью 75000 успешно приобретен.')
#   bank -= 75000
#   if bank < 5000:
#     bank += 1000
#     print('Сделана скидка в размере ', 1000)
# else:
#   print('Не хватает денег на счёте!')
# print('Остаток на счету:', bank)
# print('Хорошего дня!')



# password = int(input('Введите пароль: '))
# a = 0
# # a = 1
# if (password == 536):
#   print('Верный пароль!')
#   a = 15
# print(a)
  


# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))
# sum = int(input('Введите сумму первого и второго чисел: '))
# if sum == num_1 + num_2:
#   print('Ответ верный!')
# else:
#   print('Ответ неверный!')

# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))
# sum = int(input('Введите сумму первого и второго чисел: '))
# if sum != num_1 + num_2:
#   print('Ответ неверный!')
# else:
#   print('Ответ верный!')




# son = int(input('Какое число я загадал? '))
# father = 5
# if son == father:
#   print('Угадал!')
#   print('Конец игры')

# son = int(input('Какое число я загадал? '))
# father = 7
# if son != father:
#   print('Не угадал!')
#   print('Конец игры')



# bank = int(input('Сколько денег на счету? '))
# if bank >= 75000:
#   print('Курс успешно приобретен.')
#   bank -= 75000
# else:
#   print('Не хватает денег на счёте!')
# print('Хорошего дня!')

# apple = int(input('Доход от яблок: '))
# orange = int(input('Доход от апельсинов: '))
# expanses = int(input('Расходы: '))
# if apple + orange > expanses:
#   print('Доходы превышают расходы.')
# else:
#   print('Доход слишком мал')



#print('Задача № 2:')
#apart_build = int(input('Введите число: ')) # последняя цифра будет номер дома, цифры с первой до предпоследней - номер квартиры
#print('Номер дома:', apart_build % 10)
#print('Номер квартиры:', apart_build // 10)


#print('Задача № 1:')
#apples = 41
#boxes = 3
#full_boxes = apples // boxes
#print('Количество полных ящиков: ', full_boxes)
#rest_apples = apples % boxes
#print('Осталось яблок: ', rest_apples, 'тонн/тонны')


#a = '2'
#b = '5'
#c = '3'
#num = 6 ** int(a) + (7 - int(b)) * int(c)
#print(num)

#print('Задачи № 1-2:')
#a = int(input('Введите первое число: '))
#b = int(input('Введите первое число: '))
#c = int(input('Введите первое число: '))
#d = int(input('Введите первое число: '))
#rez = 2 * ( (c + 5 + (a * b) / (4 * b)) * (d - 2 * ((a ** 3) / 30)) ) - 10
#print('Сумма =', rez)
#print()


#print('такое же решение этой задачи, но с кодом в одну строку:')
#print('Сумма =', int(input('Введите первое число: ')) + int(input('Введите второе число: ')))

#a = int(input('Введите первое число: '))
#b = int(input('Введите первое число: '))
#c = a + b
#print(c)
#a, b = '12', '34'
#print(int(a + b) * 2)

#print('Задача № 1')
#a, b, c = 8, 5, 3
#print('Ответ:', (a / (b + c) - a)/c)
#print()
#print('---------------')
#print()
#print('Задача № 2')
#bus = 5
#metro = 3
#result = (6 + (10 - bus) ** 2) / (metro + 1) + 132 / (2 + bus)
#print('Ответ:', result)
#print()
#print('---------------')
#print()
#print('Задача № 3')
#value = (-3 + (8 ** 2 - 12) * 4 ** 3 ** 2) / (2 * 18)
#print('Ответ:', value)

#a, b, c = 8, 5, 3
#print(a + b + c)
#print(a - b - c)
#print(a * b * c)
#print(a / b / c)
#print(a ** b ** c)
#print(65 / 0) #ZeroDivisionError: division by zero

#print(6 * 39)
#print(3 ** 5)
#print(-8 / -4)
#print(10 / 2 + 6)

#a = -5
#b = 7

# import task_1
# import task_2
# import task_3
# import task_4
# import task_5
# import task_6

#name = input('Введите имя: ')
#print('Привет,', name + '. Я - компьютер')
#print()
#name2 = input('Введите второе имя: ')
#print('Привет,', name2 + '. Я - компьютер')
#print()
#name1, name2, name3 = 'Вова', 'Петя', 'Лена'
#print(name1 + ', ' + name2 + ', ' + name3)

#numbers = [1, 5, 9, 6]
#numbers.pop(0)  # 0 (zero) index is deleted
#print(numbers)
#numbers = [1, 2, 3, 4]
#numbers.pop()  # without any arguments the method deletes the last element
#print(numbers)

#print('login as: zabbbix')
#print('Zabbix server Appliance (mysql)')
#print("zabbix@192.168.2.5's password:")
#print('Last login: Fri Feb 17 13:00:10 2023 from 192.168.2.3')
#print('########   ###    #######  #######  #### ##     ##')
#print('     ##   ## ##   ##    ## ##    ##  ##   ##   ##')
#print('    ##   ##   ##  ##    ## ##    ##  ##    ## ##')
#print('   ##   ##     ## #######  #######   ##     ### ')
#print('  ##    ######### ##    ## ##    ##  ##    ## ##')
#print(' ##     ##     ## ##    ## ##    ##  ##   ##   ##')
#print('####### ##     ## #######  #######  #### ###    ##')
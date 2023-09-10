print('Задача 1. Космическая еда')

# Ваш космический корабль потерпел крушение на пустынной планете. Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки. Из прошлого опыта вы знаете, что если будете экономно питаться, то у вас будет уходить по четыре килограмма гречки в месяц.

# Чтобы прикинуть гречневый бюджет, вы решили написать программу, которая выведет информацию о том, сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее, пока она не закончится. Используйте цикл for.

total_supply = int(input('Сколько осталось гречки? '))
print()
month = 0
for supply in range(total_supply, 0, -4):
  month += 1
  print('Через', month, 'мес. останется', supply - 4, 'кг гречки')
print('Запасы гречки закончатся через', month, 'месяцев.')

print()
print('-------------')
print()
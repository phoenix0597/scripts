print('Задача 1. Я стал новым пиратом!')

# Старому капитану нужно пополнить команду, но на корабль попадут только достойные! Он отобрал десять человек. Те, кто крикнет слово «Карамба», попадут на борт.

# Что нужно сделать

# Пользователь вводит десять слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».

pirates_count = 0
for candidate in range(10):
  answer = input('Что кричат пираты? ')
  if answer == 'Карамба':
    pirates_count += 1
print('\nКоличество человек, прошедших собеседование на вакансию пирата:', pirates_count)

print('\n--------\n')  
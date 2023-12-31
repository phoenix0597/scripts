print('Задача 7. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

from random import randint

def rock_paper_scissors():
  # игра "Камень, ножницы, бумага"
  gameList = ['камень', 'ножницы', 'бумага']
  random_index = randint(0, 2)
  hidden_answer = gameList[random_index]
  # print('hidden_answer =', hidden_answer)
  answer = input('\nКамень, ножницы или бумага? ')
  
  # ответ и загаданное число совпали - ничья
  if answer.lower() == hidden_answer:
    print('Ничья!')
  # программа загадала камень
  elif (hidden_answer == 'камень') and (answer.lower() == 'ножницы'):
    print('Вы проиграли!')
  elif (hidden_answer == 'камень') and (answer.lower() == 'бумага'):  
    print('Вы выиграли!')
  # программа загадала ножницы
  elif (hidden_answer == 'ножницы') and (answer.lower() == 'бумага'):
    print('Вы проиграли!')
  elif (hidden_answer == 'ножницы') and (answer.lower() == 'камень'):  
    print('Вы выиграли!')  
  # программа загадала бумага
  elif (hidden_answer == 'бумага') and (answer.lower() == 'камень'):
    print('Вы проиграли!')
  elif (hidden_answer == 'бумага') and (answer.lower() == 'ножницы'):  
    print('Вы выиграли!')    
  else:
    print('Ошибка ввода: можно вводить только "камень", "ножницы" или "бумага"')  
  
  repeat = int(input('Хотите повторить? \n("да" - 1, "нет" - любое другое число): '))
  if repeat == 1:
    rock_paper_scissors()
  else:
    print('\nДо свиданья!')

def guess_the_number():
  # игра "Угадай число"
  hidden_number = randint(1, 10)
  print('hidden_number =', hidden_number)
  user_number = int(input('Угадайте целое положительное число от 1 до 10: '))
  while user_number != hidden_number:
    user_number = int(input('Ответ неверный. Попробуйте еще раз: '))
  else:
    print('Вы угадали! Да, это', user_number)
    

def mainMenu():
  # главное меню игры
  print('1. Играть в "Камень, ножницы, бумага"')
  print('2. Играть в "Угадай число"')
  choice = int(input('\nВыберите игру: '))
  if choice == 1:
    rock_paper_scissors()
  elif choice == 2:
    guess_the_number()
  else:
    print('Ошибка ввода: нужно ввести 1 или 2.')  

mainMenu()
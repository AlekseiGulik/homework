#todo: Дописать игру "Поле чудес"
# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
# words = ["оператор", "конструкция", "объект"]
# desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.
#
# Пример вывода:
#
# "Это слово обозначает наименьшую автономную часть языка программирования"
#
# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒
#
# Введите букву: O
#
# O  ▒  ▒  ▒  ▒  ▒  O  ▒
#
#
# Введите букву: Я
#
# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:


from random import randint as ri
words: None
desc_: None
attempt = 0
def init():
    global words, desc_
    words = ["operator", "constract", "object"]
    desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования.",
               "Это синтаксическая структура, которая определяет способ организации кода.",
               "Это сущность, представляющая собой экземпляр класса." ]
def get_attemt():
    return attempt

def set_attemt():
    global attempt
    attempt += 1

def get_word():
    global words
    word_index = ri(0, len(words) - 1)
    print_(word_index)
    return words[word_index]

def print_(word_index):
    global desc_
    print("Угадайте слово по подсказке: " + desc_[word_index] + "\n")

def get_field(word_for_play):
     return [" ▒"] * len(word_for_play)

def get_letter():
    letter = input(f"\nУ вас осталось {10 - get_attemt()} попыток! \nВведите букву: ")
    return letter

def engine(word_for_play,player_word):
    pass

def game():
    init()
    word_for_play = get_word()
    player_word = get_field(word_for_play)
    print("".join(player_word))
    engine(word_for_play, player_word )


print('''
*******************************
********* ПОЛЕ ЧУДЕС **********

1. Начать игру !
2. Выйти.

''')

key = int(input('Ваш выбор % '))

match key:
    case 1:
        game()
    case 2:
        exit(0)
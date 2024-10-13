# todo: База данных пользователя.
# Задан массив объектов пользователя

# Написать фильтр, который будет выводить отсортированные объекты по возрасту(больше введённого), первой букве логина, и заданной группе.

# Фильтр по условиям
# def filter_users(users, min_age, login_letter, group_name):
#
#     filtered_users = []
#     for user in users:
#         if user['age'] > min_age:
#             if user['login'].startswith(login_letter):
#                 if user['group'] == group_name:
#                     filtered_users.append(user)
#     sorted_users = sorted(filtered_users, key=lambda user: user['age'])
#     return sorted_users
#
users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# min_age = int(input('Введите возраст: '))
# login_letter = input('Введите первую букву имени: ')
# group_name = input('Введите группу: ')
#
# result = filter_users(users, min_age, login_letter, group_name)
# print(result)

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
#
# Затем сообщение для ввода.
# Введите критерии поиска: 16
#
# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"



# Простая сортировка

# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# sorted_users = sorted(users, key=lambda user: (user['age'], user['login'], user['group']))
#
# print(sorted_users)

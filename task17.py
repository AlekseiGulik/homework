#todo: Заданы множества

all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'} # все пользователи
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'} # пользователи не в сети
online_users = all_users - offline_users # Вычислить пользователей online
print(online_users)

#todo: Заданы множества

readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1' } #Даны читатели книг
readers_magazines = { 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'} #Даны читатели газет
readers_all = readers_books & readers_magazines # Найти пользователей кто читает и книги и газеты
if readers_all:
    print('Читают и книги и газеты: ')
else:
    print('Никто не читает и книги и газеты: ')





#todo: Дан массив размера N. Найти минимальное расcтояние между одинаковыми значениями в массиве и вывести их индексы.

# Пример:
print('Дан массив:[1,2,17,54,30,89,2,1,6,2]')
min_dist = int(input('Введите число из массива: '))
mass = [1,2,17,54,30,89,2,1,6,2]
index = {}
indices = (-1, -1)

for i, numbers in enumerate(mass):
    if numbers == min_dist:
        if numbers in index:
            dist = i - index[numbers]
            if dist < min_dist:
                min_dist = dist
            indices = (index[numbers], i)
    index[numbers] = i
if indices == (-1, -1):
    print('Для этого числа нет минимального расстояния т.к элемент в массиве один.')
else:
    print(min_dist, indices)

# Для числа 1 минимальное расcтояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное раcстояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального расcтояния т.к элемент в массиве один.

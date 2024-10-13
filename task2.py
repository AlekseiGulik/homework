# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
from lesson_1.home_task.task1 import boolean

age = "23"
age = int(age)
print(type(age))

foo = "23abc"
foo = int(foo)
print(type(foo)) #Возникает ошибка: что строка содержит нечисловые символы, поэтому её невозможно преобразовать в int

# Преобразуйте переменную age в Boolean
# age = "123abc"

age = "123abc"
age = bool(age)
print(type(age))

# Преобразуйте переменную flag в Boolean
# flag = 1
flag = 1
flag = bool(flag)
print(type(flag), bool(flag))

# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
str_one = "Privet"
str_one = bool(str_one)
print(type(str_one), bool(str_one))

str_two = ""
str_two = bool(str_two)
print(type(str_two), bool(str_two))

# Преобразуйте значение 0 и 1 в Boolean
x = bool(0)
print(x)
y = bool(type(1))
print(type(y))

#
# Преобразуйте False в строку
f = str(False)
print(type(f))
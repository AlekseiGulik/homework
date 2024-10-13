#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result_summ = a + b
print("Сумма:", result_summ)

result_sub = a - b
print("Разность:", result_sub)

result_divide = a / b
print("Частное:", result_divide)

result_mult = a * b
print("Произведение:", result_mult)

result_divide_1 = a // b
print("Результат целочисленного деления:", result_divide_1)

result_divide_2 = a % b
print("Результат деления с остатком:", result_divide_2)

result_squared = a ** b
print("Результат возведения в степень:", result_squared)
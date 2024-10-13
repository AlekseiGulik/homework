# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

year = int(input("Введите год: "))
def get_century(year):
    if year % 100 == 0:
        century = year // 100
    else:
        century = (year // 100) + 1
    return century
century = get_century(year)
print(f"{year} год соответствует {century} столетию.")

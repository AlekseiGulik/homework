#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................


def count_vowels_in_text(text, vowels):
    vowel_count = {vowel: 0 for vowel in vowels}

    for char in text:
        if char in vowel_count:
            vowel_count[char] += 1
    return vowel_count


f = open("dump.txt", "r", encoding="utf-8")
text = f.read()

vowels = "аеёиоуыэюя"

vowel_count = count_vowels_in_text(text, vowels)

for vowel, count in vowel_count.items():
    print(f"Буква '{vowel}' встречается {count} раз(а) в тексте.")
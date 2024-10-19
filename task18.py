#todo: Модифицировать программу таким образом чтобы она выводила
#  приветствие "Hello", которое до этого записано в файл text.txt
#  через метод write()

f = open("text.txt", "w+t")
f.write("Hello\n")
f.seek(0) # переместит указатель в начало строки
first_line = f.readline().strip() # вычитка первой строки
print(first_line)
# print(f.write(str(None) + "\n"))


# #todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id - номер по порядку (от 1 до 10);
# – текст из списка algoritm
#
# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
# "EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
#
# Каждое значение из списка должно находится на отдельной строке.
# Выход:
# 1 % "C4.5"
# 2 % "k - means"
# и т.д.

import csv

file_name = "algoritm.csv"

id_ = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
algo = ["C4.5", "k-means", "Метод опорных векторов",
        "Apriori", "EM", "PageRank", "AdaBoost", "kNN",
        "Наивный байесовский классификатор", "CART"]

f = open(file_name, 'w', newline='', encoding='utf-8')

writer = csv.writer(f)

writer.writerow(['ID', 'Algorithm'])

for i in range(len(id_)):
    writer.writerow([id_[i], algo[i]])

f.close()


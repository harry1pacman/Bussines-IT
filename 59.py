#имя проекта: task 50


#номер версии: 1.0



#имя файла: 50task



#автор и его учебная группа: Pollak Igor, ЭУ-120



#дата создания: 20.12.2019



#дата последней модификации: 20.12.2019



#связанные файлы: - numpy


#описание: Подсчитать количество чисел, делящихся на 3 нацело


#версия Python: 3.8


import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]

for i in range(M):
    arr[i] = input()
m = 0
for i in range(M):
    for n in range(len(arr[i])):
        S = arr[i]
        if S[n] == " ":
            m += 1
    print("Количество пробелов " + "\"" + str(arr[i]) + " \" " + " равно " + str(m))

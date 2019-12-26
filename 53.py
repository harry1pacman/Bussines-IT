#имя проекта: task 31



#номер версии: 1.0



#имя файла: 31task



#автор и его учебная группа: Pollak Igor, ЭУ-120



#дата создания: 20.12.2019



#дата последней модификации: 20.12.2019



#связанные файлы: - 



#описание: Подсчитать количество гласных букв в каждой из заданных строк.



#версия Python: 3.8


import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]
m = 0

for i in range(M):
    arr[i] = input()

for i in range(M):
    m = 0
    for n in range(len(arr[i])):
        S = arr[i]
        if S[n] == "а" or S[n] == "е" or S[n] == "ё" or S[n] == "и" or S[n] == "о" or S[n] == "у" or S[n] == "ы" or S[n] == "э" or S[n] == "ю" or S[n] == "я":
            m += 1

    print("Количество глассных букв в слове " + "\"" + str(arr[i])+ "\"" + " равно "  + str(m))

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

import numpy



N = int(input("Количество элементов в массиве "))

A = [random.randint(-5, 5) for i in range(0, N)]

print(A)

S = 0

K = 0

L = 0



for i in range(N):

    if A[i]%3 == 0:

        S = S + 1

    if A[i]%2 == 0:

        K = K + 1

        L = L + A[i]

F = L/K



A.append(F)

A.insert(0,S)

print(F)

print(S)

print(A)

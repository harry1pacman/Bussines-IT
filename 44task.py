
#имя проекта: task 44



#номер версии: 1.0



#имя файла: 44task



#автор и его учебная группа: Pollak Igor, ЭУ-120



#дата создания: 26.12.2019



#дата последней модификации: 26.12.2019



#связанные файлы: - numpy



#описание: сортировка массива «методом пузырька».



#версия Python: 3.8

import random

import numpy as np



N = int(input("Количество элементов массива "))

A = [random.randint(-10,10) for i in range(0,N)]

print(A)

Ao = []

Ap = []





for i in range(N):

    if A[i] > 0:

        Ap.append(A[i])

    if A[i] < 0:

        Ao.append(A[i])



sumAo = np.size(Ao)

sumAp = np.size(Ap)

Q = sumAo-sumAp

W = sumAp - sumAo

print(sumAo)

print(sumAp)



if sumAo == sumAp:

    print("Количество отрицательных и положительных элементов массива равно")

if sumAo > sumAp:

    A.append([random.randint(1,10) for i in range(0,Q)])

if sumAp > sumAo:

    A.append([random.randint(-1, -10) for i in range(0,W)])



print(A)

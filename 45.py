#имя проекта: task 31



#номер версии: 1.0



#имя файла: 31task



#автор и его учебная группа: Pollak Igor, ЭУ-120



#дата создания: 20.12.2019



#дата последней модификации: 20.12.2019



#связанные файлы: - numpy



#описание: Добавить к элементам массива такой новый элемент



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



sumAo = np.sum(Ao)

sumAp = np.sum(Ap)

sumAo = abs(sumAo)

Q = (sumAo-sumAp)

print(sumAo)

print(sumAp)

print(Q)



if sumAo == sumAp:

    print("Сумма отрицательных и положительных элементов массива равно")

if sumAo > sumAp:

    A.append([Q])

if sumAp > sumAo:

    A.append([Q])



print(A)

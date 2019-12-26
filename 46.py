
#имя проекта: task 46



#номер версии: 1.0



#имя файла: 46task



#автор и его учебная группа: Pollak Igor, ЭУ-120



#дата создания: 20.12.2019



#дата последней модификации: 20.12.2019



#связанные файлы: - numpy



#описание: Разделить число между положительными элементами массива



#версия Python: 3.8

import random

import numpy

N = int(input("Количество элементов массива "))

T = int(input("Положительное число "))

A = [random.randint(-10, 10) for i in range(0, N)]

print(A)



S = 0



for i in range(N):

    if A[i] > 0:

        S = S + A[i]



K = T/S



for i in range(N):

    if A[i] > 0:

        A[i] += (A[i]*K)



print(K)

print(A)

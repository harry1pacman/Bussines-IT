
#имя проекта: task 43



#номер версии: 1.0



#имя файла: 43task



#автор и его учебная группа: Pollak Igor, ЭУ-120



#дата создания: 20.12.2019



#дата последней модификации: 20.12.2019



#связанные файлы: - numpy


#описание: Из элементов исходного массива построить два новых.



#версия Python: 3.8

import random

import numpy as np



N = int(input("Количество элементов массива "))

A = [random.randint(-10,10) for i in range(0,N)]

Ao = []

Ap = []





for i in range(N):

    if A[i] > 0:

        Ap.append(A[i])

    if A[i] < 0:

        Ao.append(A[i])



print("Отрицательные",Ao)

print("Положительные ",Ap)

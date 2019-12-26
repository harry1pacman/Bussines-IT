#имя проекта: task 37



#номер версии: 1.0



#имя файла: 37task



#автор и его учебная группа: Pollak Igor, ЭУ-120



#дата создания: 23.12.2019



#дата последней модификации: 23.12.2019



#связанные файлы: - numpy/array



#описание: Сумму элементов массива и количество положительных элементов поставить на первое и второе место.



#версия Python: 3.8

import numpy 

import array

import random



N = int(input("Введите количество элементов массива "))

A = [random.randint(-20, 20) for i in range(0, N)]

print(A)

B = 0



cym = numpy.sum(A)

C = numpy.size(A)

for i in range(N):

    if A[i] >= 0:

        B += A[i]

(A.insert(0, B))

(A.insert(1, C))

print(A)

#имя проекта: task 38



#номер версии: 1.0



#имя файла: 38task



#автор и его учебная группа: Pollak Igor, ЭУ-120



#дата создания: 23.12.2019



#дата последней модификации: 23.12.2019



#связанные файлы: - numpy/array



#описание: Исключить M элементов, начиная с позиции K.



#версия Python: 3.8

import numpy as np

import array

import random


N = int(input("Введите количество элементов массива "))

K = int(input("Позиция K "))

M = int(input("количество элементов для вычитания "))

A = [random.randint(0, 100) for i in range(0, N)]


print(A)


A.insert(K,M)

print(A)



A.delete(K,M)

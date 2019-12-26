#номер версии: 1.0

#имя файла: 68

#автор и его учебная группа: Pollak Igor, ЭУ-120

#дата создания: 19.12.2019

#дата последней модификации: 19.12.2019

#связанные файлы: - math

#описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Найти наибольшее значение среди средних значений для каждой строки матрицы. 

#версия Python: 3.8

import random
import math
M = random.randint(1,5)
print("M = " + str(M))
N = random.randint(1,5)
print("N = " + str(N))
mat = [[random.randint(0,10) for y in range(M)] for i in range(N)]

for i in range(N):
    print(mat[i])

def maxaverline(mat):
   return max(sum(line) / len(line) for line in mat)
print("Ответ: " + str(maxaverline(mat)))

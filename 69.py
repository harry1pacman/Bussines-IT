#имя проекта: task 69

#номер версии: 1.0

#имя файла: 69

#автор и его учебная группа: Pollak Igor, ЭУ-120

#дата создания: 26.12.2019

#дата последней модификации: 26.12.2019

#связанные файлы: math

#описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
#Найти наименьший элемент столбца матрицы A, для которого сумма абсолютных значений элементов максимальна. 


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

c=[]
for num, j in enumerate(mat[0]):
    b=0
    for n in mat:
        b = b + math.fabs (n[num])
    c.append(b)

print("Ответ: " + str(min(c)))

#имя проекта: task 78

#номер версии: 1.0

#имя файла: 78

#автор и его учебная группа: Pollak Igor, ЭУ-120

#дата создания: 30.12.2019

#дата последней модификации: 30.12.2019

#связанные файлы: 

#описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов 

#версия Python: 3.8


import random

N = 5  # строк
M = 7  # столбцов

L = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

i = 0
while i < len(A):
    j = 0
    max_element = max(A[i])
    while j < len(A[i]):
        A[i][j] /= max_element
        A[i][j] = round(A[i][j], 1)
        j += 1

    i += 1

print("Модифицированная матрица:")
print_matrix(A)

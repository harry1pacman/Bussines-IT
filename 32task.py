#имя проекта: task 32

#номер версии: 1.0

#имя файла: 32task

#автор и его учебная группа: Pollak Igor, ЭУ-120

#дата создания: 21.12.2019

#дата последней модификации: 21.12.2019

#связанные файлы: - 

#описание: Поменять местами элементы, стоящие на чётных и нечётных местах

#версия Python: 3.8

import random

import sys

n = 25

a = [random.randint(0, 100) for i in range(0,n)]

print(a)



if (len(a) % 2 == 1):

    end = n

else:

    end = n-1





for i in range(0, end-1, 2):

    a[i], a[i + 1] = a[i + 1], a[i]

print(a)

#имя проекта: task 66

#номер версии: 1.0

#имя файла: 66

#автор и его учебная группа: Pollak Igor, ЭУ-120

#дата создания: 19.12.2019

#дата последней модификации: 19.12.2019

#связанные файлы: - 

#описание: Для вводимых чисел определить процент положительных и отрицательных чисел. 


#версия Python: 3.8

import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]
n = 0
m = 0
N = 65432
for i in range(M):
    arr[i] = input()

for i in range(M):
    if int(arr[i]) > 0:
        n += 1
    if int(arr[i]) < 0:
        m += 1
    if int(arr[i]) == 65432 :
        break
print("Процент положительных чисел: " + str(100 / len(arr) * n ))
print("Процент отрицательных чисел: " + str(100 / len(arr) * m ))

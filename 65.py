#имя проекта: task 65

#номер версии: 1.0

#имя файла: 65

#автор и его учебная группа: Pollak Igor, ЭУ-120

#дата создания: 26.12.2019

#дата последней модификации: 26.12.2019

#связанные файлы: - 

#описание: Определить сумму чисел, делящихся на положительное число B нацело

#версия Python: 3.8

import random
B = random.randint(1,10)
print("B = " + str(B))
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]
a = 0


for i in range(M):
    arr[i] = input()

for i in range(M):
    if int(arr[i]) < 0:
        print("END")
        break
    elif int(arr[i]) % B == 0:
        a += int(arr[i])
print("Конечный результат " + str(a))

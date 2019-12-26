#имя проекта: task 64

#номер версии: 1.0

#имя файла: 64

#автор и его учебная группа: Pollak Igor, ЭУ-120

#дата создания: 26.12.2019

#дата последней модификации: 26.12.2019

#связанные файлы: - 

#описание: Суммировать вводимые числа, среди которых нет нулевых

#версия Python: 3.8

import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]
a = 0


for i in range(M):
    arr[i] = input()

for i in range(M):
    if int(arr[i]) == 99999:
        print("END")
        break
    elif int(arr[i]) == 0:
       print(a)
    elif int(arr[i]) > 0:
        a += int(arr[i])
print("Конечный результат " + str(a))

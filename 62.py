#имя проекта: task 62

#номер версии: 1.0

#имя файла: 62

#автор и его учебная группа: Pollak Igor, ЭУ-120

#дата создания: 26.12.2019

#дата последней модификации: 26.12.2019

#связанные файлы: - 

#описание: Определить сумму вводимых положительных чисел

#версия Python: 3.8

import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]
a = 0
b = 0
n = 0
m = 0

for i in range(M):
    arr[i] = input()

for i in range(M):
    if int(arr[0]) < 0:
        print("END")
        break
    elif i % 2 == 0:
       b += -(int(arr[i]))
       m += 1
    elif i % 2 != 0:
        a += (int(arr[i])) ** 2
        n += 1
print(" числа с нечётными номерами суммировать с обратным знаком:" + str(b))
print("количество слагаемых: " + str(m))
print("числа с чётными номерами перед суммированием возводить в квадрат: " + str(a))
print("количество сомножителей: " + str(n))
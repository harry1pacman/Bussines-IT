#имя проекта: task 61

#номер версии: 1.0

#имя файла: 61

#автор и его учебная группа: Pollak Igor, ЭУ-120

#дата создания: 26.12.2019

#дата последней модификации: 26.12.2019

#связанные файлы: - 

#описание: Подсчитать количество слагаемых и количество сомножителей

#версия Python: 3.8
import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]
a = 1
b = 0
n = 0
m = 0

for i in range(M):
    arr[i] = input()

for i in range(M):
    if int(arr[i]) == 55555:
        print("END")
        break
    elif i% 2 == 0:
        a *= int(arr[i])
        n += 1
    elif i % 2 != 0:
        b += int(arr[i])
        m += 1
print("сумму чисел с нечётными номерами:" + str(b))
print("количество слагаемых: " + str(m))
print("произведение чисел с чётными номерами: " + str(a))

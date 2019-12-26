#имя проекта: task 52



#номер версии: 1.0



#имя файла: 52task



#автор и его учебная группа: Pollak Igor, ЭУ-120



#дата создания: 20.12.2019



#дата последней модификации: 20.12.2019



#связанные файлы: - 



#описание: составить одну длинную строку, разделяя слова пробелами.



#версия Python: 3.8

import random
M = random.randint(1,10)
arr = [random.randint(1,10) for i in range(M)]

for i in range(M):
    arr[i] = input()
print(arr)
b = arr[0]

for i in range(1 , M):
    b = str(b) + " " + arr[i]
print(b)

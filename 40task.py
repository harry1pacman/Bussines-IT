#имя проекта: task 40



#номер версии: 1.0



#имя файла: 40task



#автор и его учебная группа: Pollak Igor, ЭУ-120



#дата создания: 20.12.2019



#дата последней модификации: 20.12.2019



#связанные файлы: - 



#описание: После каждого отрицательного элемента вставить новый элемент



#версия Python: 3.8



import random



N = int(input("Количество элементов массива "))

A = [random.randint(-10,10) for i in range(0, N)]

print(A)



for i in range(N):

    if A[i] < 0:

        A[i] = A[i]**2

print(A)

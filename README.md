# Bussines-IT
101 задача по программированию
7 задача:
n=int(input())
if n%2 ==0 :
    if n%4 ==0 :
        print(n, 'кратно 2 и 4')
    else:
        print(n, 'кратно 2 но не кратно 4')
else:
    print(n, 'не кратно 2 и не кратно 4')
8 задача:
n=int(input())
if n%2 == 1 :
    if n%5 == 0 :
        print(n, 'нечетное и кратно 5 ')
    else:
        print(n, 'не удовлетворяет условию')
else:
    print(n, 'не соответсвует условию')
Задача 9:
n=int(input())
if n%2 == 1 :
    if n%7 == 0 :
        print(n, 'нечетное и кратно 7 ')
    else:
        print(n, 'не удовлетворяет условию')
else:
    print(n, 'не соответсвует условию')
Задача 10:
n=int(input())
if n%2 == 0 :
    if n%10 == 0 :
        print(n, 'четное и кратно 10 ')
    else:
        print(n, 'не удовлетворяет условию')
else:
    print(n, 'не соответсвует условию')
Задание  12:
n = int(input())
if n > 0:
    print('Положительное число')
elif n < 0:
    print('Отрицательное число')
elif n == 0:
    print('Число равно нулю')
задание  13:
d = int(input('бревно'))
a = int(input('брусок'))
if d**2 == a**2 + a**2:
    print('можно')
elif d**2 > a**2 + a**2:
    print('можно')
else:
    print('нельзя')
    задание 20:
    x = int(input())
a = int(input())
b = int(input())
if a <= x and b >= x:
    print('входит')
else:
    print('не входит')
    задание 21:
x = int(input())
y = int(input())
z = 1/(x*y)
print(z)
    задание 22:
    a = int(input())
b = int(input())
c = int(input())
if a<b and b>c:
    print('оба неравенства верны')
else:
    if a<b:
        print('1 неравенствo вернo')
    elif b>c:
        print('2 неравенствo вернo')
    else:
        print('оба неравенства неверны')
задание 29:
    a = int(input())
if a%4 ==0:
    b = a/100 + 1
    print('викосный год, век', b)
else:
    b = a//100 + 1
    print('невикосный год, век', b)
задание 16:
 a = int(input())
if a%2 == 0:
    b = a//500
    c = (a-500*b)//100
    d = (a-500*b-100*c)//10
    e = (a-500*b-100*c-10*d)//2
    print(b, 'купюр по 500', c, 'купюр по 100', d, 'купюр по 10',  e, 'монет по 2',) 
else:
    print('размен невозможен')
    задание 25:
    a = int(input())
if a<=2:
    f = a**2 + 4*a + 5
    print(f)
else:
    f = 1 / (a**2 + 4*a + 5)
    print(f)
задание 26:
        a = float(input())
if a==0:
    f = 0
    print(f)
elif 0 < a and a < 1:
    f = a**2 - a
    print(f)
else:
    f = a**4
    print(f)      
   

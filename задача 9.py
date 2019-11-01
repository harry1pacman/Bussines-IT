n=int(input())
if n%2 == 1 :
    if n%7 == 0 :
        print(n, 'нечетное и кратно 7 ')
    else:
        print(n, 'не удовлетворяет условию')
else:
    print(n, 'не соответсвует условию')

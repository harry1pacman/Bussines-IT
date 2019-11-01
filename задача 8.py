n=int(input())
if n%2 == 1 :
    if n%5 == 0 :
        print(n, 'нечетное и кратно 5 ')
    else:
        print(n, 'не удовлетворяет условию')
else:
    print(n, 'не соответсвует условию')

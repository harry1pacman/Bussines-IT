n=int(input())
if n%2 == 0 :
    if n%10 == 0 :
        print(n, 'четное и кратно 10 ')
    else:
        print(n, 'не удовлетворяет условию')
else:
    print(n, 'не соответсвует условию')

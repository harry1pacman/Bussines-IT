a = int(input())
if a%2 == 0:
    b = a//500
    c = (a-500*b)//100
    d = (a-500*b-100*c)//10
    e = (a-500*b-100*c-10*d)//2
    print(b, 'купюр по 500', c, 'купюр по 100', d, 'купюр по 10',  e, 'монет по 2',) 
else:
    print('размен невозможен')

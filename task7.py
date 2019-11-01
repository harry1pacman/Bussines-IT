n=int(input())
if n%2 ==0 :
    if n%4 ==0 :
        print(n, 'кратно 2 и 4')
    else:
        print(n, 'кратно 2 но не кратно 4')
else:
    print(n, 'не кратно 2 и не кратно 4')

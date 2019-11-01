a = int(input())
if a%4 ==0:
    if a%100 == 0:
        b = a//100
    else:
        b = a//100 + 1
    print('викосный год, век', b)
else:
    b = a//100 + 1
    print('невикосный год, век', b)

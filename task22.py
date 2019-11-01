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

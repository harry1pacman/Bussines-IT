a = int(input())
b = int(input())
c = int(input())
if a < b and a < c:
    print (a, 'меньшее число')
elif b<a and b<c:
    print (b, 'меньшее число')
elif c<a and c<b:
    print (c, 'меньшее число')
else:
    print ('числа равны')
    

a = float(input())
if a==0:
    f = 0
elif 0 < a and a < 1:
    f = a**2 - a
else:
    f = a**4     
print(f)

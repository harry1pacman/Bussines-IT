X = int(input("Сторона 1 "))
Y = int(input("Сторона 2 "))
Z = int(input("Сторона 3 "))

if (X + Y <= Z) or (Y + Z <= X) or (Z + X <= Y):
    print("Треугольник с такими сторонами не существует")
    import sys
    sys.exit(0)


if (X > Y and X > Z) and (X**2 == Y**2 + Z**2):
    print("Труегольник прямоугольный")
elif (Y > X and Y > Z) and (Y ** 2 == X ** 2 + Z ** 2):
    print("Труегольник прямоугольный")
elif (Z > Y and Z > X) and (Z ** 2 == Y ** 2 + X ** 2):
    print("Труегольник прямоугольный")
else:
    print("Труегольник не прямоугольный")

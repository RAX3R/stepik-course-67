x = str(input())

if x == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())

    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    print(s)

elif x == "прямоугольник":
    a = float(input())
    b = float(input())

    s = a * b

    print(s)

elif x == "круг":
    r = float(input())

    pi = 3.14
    s = pi * (r ** 2)

    print(s)

a = int(input())

if 0 <= a <= 1000:
    ost = a % 10
    if a % 10 == 0 or 5 <= a % 10 <= 9 or 11 <= a % 100 <= 19:
        print(a, "программистов")
    elif a % 10 == 1 and not (11 <= a % 100 <= 19):
        print(a, "программист")
    elif 2 <= a % 10 <= 4:
        print(a, "программиста")

a = str(input())

q = int(a[0])
w = int(a[1])
e = int(a[2])
r = int(a[3])
t = int(a[4])
y = int(a[5])

if (q + w + e) == (r + t + y):
    s = "Счастливый"
else:
    s = "Обычный"

print(s)

a = int(input())
b = int(input())

s = 0
x = 0
r = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        x += 1
    if x > 0:
        r = s / x

print(r)

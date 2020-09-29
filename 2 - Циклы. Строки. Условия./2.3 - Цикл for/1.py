a = int(input())
b = int(input())
c = int(input())
d = int(input())

f = ''

for i in range(c, d + 1):
    print('\t', i, end='')
print()

for ii in range(a, b + 1):
    print(ii, end="")
    for j in range(c, d + 1):
        f = str(ii * j)
        print('\t', f, end='')
    print()

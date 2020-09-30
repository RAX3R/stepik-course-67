a = str(input())

f = 0

for i in a:
    if i == 'c' or i == 'C' or i == 'G' or i == 'g':
        f += 1

s = (f / len(a)) * 100

print(s)

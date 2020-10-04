summa = int(input())

c = 0
kv = summa ** 2

if summa == 0 and c == 0:
    summa = 0
    kv = 0
else:
    while summa != 0:
        input_data = int(input())
        summa += input_data
        c += 1
        kv += input_data ** 2

print(kv)

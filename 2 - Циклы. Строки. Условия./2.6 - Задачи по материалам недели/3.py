lst = input().split()
x = input()

if x not in lst:
    print("Отсутствует")
else:
    str_out = ""

    for i, j in enumerate(lst):
        if x == j:
            str_out += str(i) + " "
    print(str_out[:-1])

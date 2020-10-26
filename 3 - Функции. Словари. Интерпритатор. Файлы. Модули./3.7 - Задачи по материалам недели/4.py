n = int(input())

point = {"север": 0, "юг": 0, "запад": 0, "восток": 0}

for i in range(n):
    input_string = input().split()
    point[input_string[0]] += int(input_string[1])

print(point['восток']-point['запад'], point['север']-point['юг'])

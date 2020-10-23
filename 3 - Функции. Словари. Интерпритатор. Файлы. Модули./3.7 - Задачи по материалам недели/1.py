n = int(input())

d = {}

for i in range(n):
    list_1 = str(input()).split(';')
    command = []
    schet = []
    for j in list_1:
        if j.isdigit():
            schet.append(int(j))
            if len(schet) > 1 and len(command) > 1:
                d[command[0]][0] += 1
                d[command[1]][0] += 1

                if schet[0] > schet[1]:
                    d[command[0]][1] += 1
                    d[command[1]][3] += 1
                    d[command[0]][4] += 3

                elif schet[0] < schet[1]:
                    d[command[1]][1] += 1
                    d[command[0]][3] += 1
                    d[command[1]][4] += 3

                elif schet[0] == schet[1]:
                    d[command[0]][2] += 1
                    d[command[1]][2] += 1
                    d[command[0]][4] += 1
                    d[command[1]][4] += 1
        else:
            command.append(j)
            if j not in d.keys():
                d.update({j: [0, 0, 0, 0, 0]})

for key, value in d.items():
  print(key, end=':')
  print(*value)

n = int(input())

list_out = []
str_out = ""
c = 0

while c < n:
    c += 1
    for j in range(c):
        list_out.append(c)

for i in range(n):
    str_out += str(list_out[i]) + " "

str_out = str_out[:-1]

print(str_out)

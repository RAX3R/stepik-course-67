s = input()

s = s + '1'
z = s[0]
c = 0
st = ''

for i in s:
    if z != i:
        st += z + str(c)
        z = i
        c = 0
    c += 1

print(st)

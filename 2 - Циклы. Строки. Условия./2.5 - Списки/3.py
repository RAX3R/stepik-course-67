string = input()

list_string = sorted(string.split())
new = []
out_str = ""

for i in list_string:
    if list_string.count(i) >= 2:
        while list_string.count(i) >= 3:
            list_string.remove(i)
        list_string.remove(i)
        new.append(i)

for j in range(int(len(new))):
    if j != 0:
        out_str += " " + new[j]
    else:
        out_str += new[j]

if len(out_str) >= 1:
    print(out_str)

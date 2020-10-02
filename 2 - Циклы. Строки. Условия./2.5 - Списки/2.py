string = input()

list_spring = string.split()
len_list = len(list_spring) - 1
new_list = []
new_string = ""

if len_list > 0:
    for i in range(len_list):
        if i == 0:
            new_list.append(int(list_spring[len_list]) + int(list_spring[i+1]))
        else:
            new_list.append(int(list_spring[i-1]) + int(list_spring[i+1]))

    new_list.append(int(list_spring[len_list - 1]) + int(list_spring[0]))
    for j in range(len_list+1):
        if j == 0:
            new_string += str(new_list[j])
        else:
            new_string += ' ' + str(new_list[j])
else:
    new_list.append(int(list_spring[0]))
    new_string = str(list_spring[0])

print(new_string)

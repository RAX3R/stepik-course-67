with open("file.txt") as inf:
    text_string = inf.readline()

int_num = ""
list_int_num = []

short_str = ""
list_short_str = []

output_text = ""

# Поиск чисел и отдельных символов:
for char in text_string:
    if char.isdigit():
        int_num += char
    else:
        if int_num != "":
            list_int_num.append(int(int_num))
            int_num = ""
        list_short_str.append(char)

if int_num != "":
    list_int_num.append(int(int_num))


for i, ii in enumerate(list_int_num):
    for x in range(int(ii)):
        output_text += list_short_str[i]

print(output_text)

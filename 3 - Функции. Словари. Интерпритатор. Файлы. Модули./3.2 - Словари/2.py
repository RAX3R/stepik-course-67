input_str = (str(input()).lower())

list_str = input_str.split()
new_dict = {}

for i in list_str:
    if i in new_dict:
        new_dict[i] += 1
    else:
        new_dict.update({i: 1})

for word, count in new_dict.items():
    print(word, count)

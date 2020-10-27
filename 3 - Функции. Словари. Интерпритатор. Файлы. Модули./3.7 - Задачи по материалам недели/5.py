with open("file - 5.txt") as inf:
    text_str = inf.readlines()
    text_string = []
    class_dict = {"1": [0, 0], "2": [0, 0], "3": [0, 0], "4": [0, 0], "5": [0, 0],
                  "6": [0, 0], "7": [0, 0], "8": [0, 0], "9": [0, 0], "10": [0, 0], "11": [0, 0]}

    for lines in text_str:
        text_string = lines.split()
        if text_string[0] in class_dict.keys():
            class_dict[text_string[0]][0] += int(text_string[2])
            class_dict[text_string[0]][1] += 1

for key, value in class_dict.items():
    if value[1] != 0:
        print(key, value[0]/value[1])
    else:
        print(key, "-")

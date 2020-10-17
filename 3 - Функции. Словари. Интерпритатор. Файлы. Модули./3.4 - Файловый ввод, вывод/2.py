with open("file2.txt") as inf:
    text_str = inf.readlines()
    text_string = ""
    for lines in text_str:
        text_string += lines.strip() + " "

new_list = []
new_word = ""
max_count = 0

# Перевод слов в список:
for char in text_string:
    if char != " ":
        new_word += char
    else:
        new_list.append(new_word.lower())
        new_word = ""

if new_word != "":
    new_list.append(new_word.lower())

max_word = new_list[0]

for word in new_list:
    if new_list.count(word) >= max_count:
        max_count = new_list.count(word)
        if len(word) < len(max_word):
            max_word = word

print(max_word, max_count)

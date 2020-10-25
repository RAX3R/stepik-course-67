count_words = int(input())
words_list = set()

for i in range(count_words):
    word = str(input()).lower()
    words_list.add(word)

count_lines = int(input())
word_for_check = set()

for j in range(count_lines):
    line = str(input().lower()).split()
    word_for_check.update(line)

for c_word in word_for_check:
    if c_word not in words_list:
        print(c_word)

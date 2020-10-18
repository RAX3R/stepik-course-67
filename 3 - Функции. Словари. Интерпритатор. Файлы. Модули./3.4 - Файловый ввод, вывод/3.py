with open("file3.txt") as inf:
    text_str = inf.readlines()
    text_string = []
    for lines in text_str:
        text_string.append(lines.strip())

rating_list = []
for txt in text_string:
    small_list = txt.split(';')
    for word in small_list:
        if word.isalpha():
            small_list.remove(word)
    rating_list.append(small_list)

m_math, m_rus, m_eng = 0, 0, 0
for i, ii in enumerate(rating_list):
    all_r = 0
    for j, jj in enumerate(ii):
        all_r += int(jj)
    m_all_r = all_r / len(ii)
    print(m_all_r)
    m_math += int(ii[0]) / len(rating_list)
    m_rus += int(ii[1]) / len(rating_list)
    m_eng += int(ii[2]) / len(rating_list)
print(m_math, m_rus, m_eng)

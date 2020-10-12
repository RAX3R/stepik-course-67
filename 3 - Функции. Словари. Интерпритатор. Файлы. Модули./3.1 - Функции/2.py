def modify_list(l):
    len_list = len(l)
    for i in reversed(range(len_list)):
        if (int(l[i]) % 2) != 0:
            l.remove(l[i])
        else:
            l[i] = int(l[i]) // 2


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6]
    print(modify_list(lst))  # None
    print(lst)  # [1, 2, 3]
    modify_list(lst)
    print(lst)  # [1]

    lst = [10, 5, 8, 3]
    modify_list(lst)
    print(lst)  # [5, 4]

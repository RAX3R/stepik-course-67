def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    elif key * 2 in d.keys():
        d[key * 2].append(value)
    else:
        d.update({key * 2: [value]})


if __name__ == '__main__':
    d = {}
    print(update_dictionary(d, 1, -1))  # None
    print(d)  # {2: [-1]}
    update_dictionary(d, 2, -2)
    print(d)  # {2: [-1, -2]}
    update_dictionary(d, 1, -3)
    print(d)  # {2: [-1, -2, -3]}

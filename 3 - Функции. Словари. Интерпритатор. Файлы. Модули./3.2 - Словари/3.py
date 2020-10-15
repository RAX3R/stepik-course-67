n_input = int(input())

new_dict = {}

for i in range(n_input):
    inp = int(input())
    if inp in new_dict:
        print(new_dict[inp])
    else:
        new_dict[inp] = f(inp)
        print(new_dict[inp])

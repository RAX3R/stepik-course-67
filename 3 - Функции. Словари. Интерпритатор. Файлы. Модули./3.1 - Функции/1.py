def f(x):
    ff = 0
    if x <= -2:
        ff = 1 - (x + 2) ** 2

    elif -2 < x <= 2:
        ff = (x / 2) * -1

    elif x > 2:
        ff = (x - 2) ** 2 + 1

    return ff

def reverse_word(x):
    y = []
    for i in x.split():
        i = i[::-1]
        y += [i]
    return " ".join(y)

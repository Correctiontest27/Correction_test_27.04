def reverse_word(x):
    y = []
    for i in x.split():
        i = i[::-1]
        y += [i]
    return " ".join(y)

# version onliner pythonique (pas demande a l'eval mais bon a savoir)
#def reverse_word(x):
#    return " ".join(w[::-1] for w in x.split())

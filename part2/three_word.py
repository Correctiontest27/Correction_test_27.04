def alpha(word):
    m = True
    alphabet = 'asdfghjklzxcvbnmiwertyuiopiWERTYUIOPLKJHGFDSAZXCVBNM'
    for i in word:
        if i not in alphabet:
            m = False
            break
    return m


def split1(value):
    l = []
    x = ''
    for i in value:
        if i == ' ':
            l += [x]
            x = ''
        else:
            x += i
    if x:
        l += [x]
    return l


def three_words(y):
    x = []
    leny = len(y)
    res = 0
    if isinstance(y, str):
        for i in split1(y):
            x = x+[i]
        lenx = len(x)
        for i in range(1, lenx-1, 1):
            if alpha(x[i-1]) and alpha(x[i]) and alpha(x[i+1]):
                res = i
                break
    elif isinstance(y, list):
        for i in range(1, leny-1, 1):
            if alpha(y[i-1]) and alpha(y[i]) and alpha(y[i+1]):
                res = i
                break
    return True if res != 0 else False

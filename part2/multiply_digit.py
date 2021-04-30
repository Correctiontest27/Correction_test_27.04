def multiply_digit(numb):
    x = ''
    y = 1
    if numb != 0:
        mark = True
        if numb < 0:
            numb = numb * -1
            mark = False
        t = str(numb)
        for i in t:
            if i != '0':
                x += i
        for i in x:
            i = int(i)
            y *= i
        y = str(y)
        if mark:
            return y
        else:
            return '-'+y
    else:
        return '0'

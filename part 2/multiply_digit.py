def digits(numb):
    l=[]
    x=''
    y=1
    if numb!=0 :
        mark=True
        if numb < 0:
            numb=numb*-1
            mark=False
        t=str(numb)
        for i in t:
            if i !='0':
                x=x+i
        lenl=len(l)
        for i in x:
            i=int(i)
            y=y*i
        y=str(y)
        if mark:
            return y
        else:
            return '-'+y
    else:
        return '0'





def Inverser(x):
    x = x.split()
    y=[]
    for i in x:
        i = i[::-1]
        y+=[i]
    return " ".join(y)

def Fizz_Buzz(y):
	if y % 3== 0 and y % 5 == 0:
		x ='fizz buzz'
	elif y % 3 == 0:
		x = 'fizz'
	elif y % 5== 0:
		x = 'buzz'
	else:
		x = i
	return x 		
			





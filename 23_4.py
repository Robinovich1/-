def f(x,y):
	z = str(x)
	if x >  y : return 0
	if x == y : return 1
	if z[-2] == '9' : return f(x+1,y)
	else :
		return f(x+1,y) + f(x+10, y)




print(f(11, 27))
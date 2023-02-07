def f(x,y):
	if x > y  : return 0
	if x == y : return 1
	b = str(x)
	if b[-2] != '9':
		return f(x+1,y) + f(x+10, y)
	else : return f(x+1,y)

print(f(11,27))
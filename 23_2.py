def f(x,y):
	if x > y  : return 0
	if x == y : return 1
	b = str(x)
	if b[-1] == "9":
		return f(x+10,y) + f(x+1,y)
	else:
		return f(x+11,y) + f(x+1,y)

print(f(25,51))
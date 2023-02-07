def f(x,y):
	if x >  y : return 0
	if x == y : return 1
	else      : return f(x+2,y) + f(x+5, y)

for y in range(100):
	if f(5, y) == 34:
		print(y)
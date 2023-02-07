def f(x,y):
	if x > y  : return 0
	if x == y : return 1
	b = str(bin(x)[2:])
	n = "1" + b
	res = int(n, 2)
	return f(x + 1,y) + f(res ,y)


print(f(0b1,0b11111))

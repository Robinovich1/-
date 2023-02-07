#F(n) = 3 при n ≤ 1
#F(n) = F(n–1) + 2·F(n–2) – 5, если n > 1

def f(n):
	if n<=1:
		return 3
	if n > 1:
		return f(n-1) + 2*f(n-2) - 5
print(f(22))
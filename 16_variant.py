import sys
sys.setrecursionlimit(2000)
#F(n) = 2, если n = 1,
#F(n) = 2 · F(n – 1), если n > 1.
def F(n):
	if n == 1:
		return 2
	if n > 1:
		return 2 * F(n-1)
print(F(1900)/ 2**1890)
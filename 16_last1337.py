from functools import lru_cache
#F(n) = 1, если n < 3
#F(n) = F(n – 2) - F(n – 1), если n > 2 и число n чётное,
#F(n) = F(n – 2) - F(n – 3), если n > 2 и число n нечётное.
@lru_cache(None)
def f(n):
	if n<3: return 1
	if n >2 and n%2 == 0: return f(n-2) - f(n - 1)
	if n >2 and n%2 != 0: return f(n-2) - f(n - 3)
print(f(50))
import math

def f(n):
	if math.sqrt(n)%1==0 and math.sqrt(n)>0: return math.sqrt(n)
	if math.sqrt(n)%1!=0 : return f(n + 1) +1

print(f(4850)+f(5000))
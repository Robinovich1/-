from functools import lru_cache
#(№ 3074) (Е. Джобс)
b = []
a = []
def moves(h):
	return (h+100), (h*2)

@lru_cache(None)
def game(h):
	if h>=1000: return "W"
	if any(game(i) == "W" for i in moves(h)): return "P1"  #i принимает два значения: H+2 или H*2
	if all(game(i) == "P1" for i in moves(h)): return "B1" 
	if any(game(i) == "B1" for i in moves(h)): return "P2" 
	if all(game(i) == "P1" or game(i) == "P2" for i in moves(h)): return "B2" 

@lru_cache(None)
def game2(h):
	if h>=1000: return "W"
	if any(game2(i) == "W" for i in moves(h)): return "P1"  
	if any(game2(i) == "P1" for i in moves(h)): return "B1" 
	




for s in range(1, 1000):
	if game(s) == 'B2':
		a.append(s)

for z in range(1, 1000):
	if game2(z) == 'B1':
		b.append(z)

for i in range(len(a)):
	for x in range(len(b)):
		if a[i] == b[x]:
			print(a[i])
	





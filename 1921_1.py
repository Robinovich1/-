from functools import lru_cache

def moves(h):
	a, b = h
	return (a+1,b), (a*4,b), (a,b+1), (a,b*4)

@lru_cache(None)
def game(h):
	a, b = h
	if a+b>=129: return "W"
	if any(game(i) == "W" for i in moves(h)): return "P1"  #i принимает два значения: H+2 или H*2
	if all(game(i) == "P1" for i in moves(h)): return "B1" # any, при неудачной игре пети
	if any(game(i) == "B1" for i in moves(h)): return "P2" 
	if all(game(i) == "P1" or games(i) == "P2" for i in moves(h)): return "B2" 

for s in range(1, 100):
	h = 4,s
	if game(h) == 'P2':
		print(s, game(h))


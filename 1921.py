from functools import lru_cache


def moves(h):
	return (h+2), (h*2)

@lru_cache(None)
def game(h):
	if h>=25: return "W"
	if any(game(i) == "W" for i in moves(h)): return "P1"  #i принимает два значения: H+2 или H*2
	if all(game(i) == "P1" for i in moves(h)): return "B1" 
	if any(game(i) == "B1" for i in moves(h)): return "P2" 
	if all(game(i) == "P1" or game(i) == "P2" for i in moves(h)): return "B2"

for s in range(1, 100):
	if game(s) == 'P2':
		print(s, game(s))


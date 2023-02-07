from functools import lru_cache

def moves(h):
	return (h+1), (h*3), (h*2)

@lru_cache(None)
def game(h):
	if 36<= h <= 60: return "W"
	if h>60: return "P1"
	if any(game(i) == "W" for i in moves(h)): return "P1"
	if all(game(i) == "P1" for i in moves(h)): return "B1"
	if any(game(i) == "B1" for i in moves(h)): return "P2"
	if all(game(i) == "P2" or game(i) == "P1" for i in moves(h)): return "B2"

for x in range(1, 100):
	if game(x) == "B2":
		print(x, game(x))

#41 3
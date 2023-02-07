from functools import lru_cache

def moves(h):
	return (h+1), (h*2)

@lru_cache(None)
def game(h):
	if 20<= h <=30: return 'W'
	if h> 30 : return "P1"
	if any(game(m) == "W" for m in moves(h)): return "P1"
	if all(game(m) == "P1" for m in moves(h)): return "B1"
	if any(game(m) == "B1" for m in moves(h)): return "P2"
	if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)): return "B2"

for h in range(1,100):
	if game(h) == "P2":
		print(h, game(h))

#16 5
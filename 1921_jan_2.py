from functools import lru_cache

def moves(h):
	return (h + 2), (h*3)

@lru_cache(None)
def game(h, n):
	if h >= n : return 'W'
	if any(game(h, n) == 'W' for m in moves(h)): return 'P1'
	if all(game(h, n) == 'P1' for m in moves(h)):
		return 'B1' break 
	if any(game(h, n) == 'B1' for m in moves(h)): return 'P2'
	if all(game(h, n) == 'P2' or game(h, n) == 'P1' for m in moves(h)): return 'B2'

for s in range(1, 100):
	if game(15, s) == 'B1':
		print(game(15, s), s)

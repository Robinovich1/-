from functools import lru_cache
def moves(h):
	return (h+1), (h*2), (h*3)

@lru_cache(None)
def game(h):
	if 36<=h<=60: return 'W'
	if h>60: return 'P1'
	if any(game(m) == 'W' for m in moves(h)): return 'P1'
	if all(game(m) == 'P1' for m in moves(h)): return 'B1'
	if any(game(m) == 'B1' for m in moves(h)): return 'P2'
	if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(h)): return 'B2'

for s in range(1, 74):
	if game(s) == "B2":
		print(s, game(s))
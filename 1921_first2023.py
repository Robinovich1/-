from functools import lru_cache

def moves(h):
	return (h*2), (h*3)

@lru_cache(None)
def game(h):
	if h >= 100: return 'W'
	if any(game(m) == 'W' for m in moves(h)):return 'P1'
	if any(game(m) == 'P1' for m in moves(h)):return 'B1'
	if any(game(m) == 'B1' for m in moves(h)):return 'P2'
	if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(h)):return 'B2'

for h in range(1,100):
	if game(h) == 'B1':
		print(h, game(h))

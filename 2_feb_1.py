print('x,y,z,w')
for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				#(x → y) ∧ (y → z) ∧ (z → w)
				if (not(x) or y) and (z or not(y)) and (not(z) or w):
					print(x,y,z,w)
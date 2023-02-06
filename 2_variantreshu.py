#((¬z ∨ w) ∧ (¬x ≡ y))→(x∧z)
print('x,y,z,w')
for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				if (((not(z) or w) and (not(x) == y))<=(x and z)) ==0:
					print(x,y,z,w)
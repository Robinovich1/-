for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				#(x ∧ (y ∨ ¬z) ∧ w) ≡ (x → ¬y ∧ z)
				if (x and (y or not(z)) and w) == (not(x) or  not(y) and z):
					print(x,y,z,w)
					



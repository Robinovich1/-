for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				if    (x and (y or not(z)) and w) == (x <= not(y) and z)      :
					# ((w → y)  ∧   (¬ x → z)) →      ((z ≡ w) ∨ (y ∧ ¬ x))
					print(x,y,z,w)
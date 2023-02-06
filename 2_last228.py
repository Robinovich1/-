print('a,b,c,d')
for a in range(2):
	for b in range(2):
		for c in range(2):
			for d in range(2):
				#(a → b) ∧ ¬(b ≡ c) ∧ (d → a)
				if (a <= b) and not(b==c) and (d<=a):
					print(a,b,c,d)
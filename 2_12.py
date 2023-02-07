print('x,y,z,w')
for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				# ((z → y) ∧ (¬ x → w)) → ((z ≡ w) ∨ (y ∧ ¬ x))
				if (((z<=y) and (x or w))<= ((z==w) or (y and not(x)))) == 0:
					print(x,y,z,w)
				# ((z → y) ∧ (¬ x → w)) → ((z ≡ w) ∨ (y ∧ ¬ x))



z = '22' + 2023*'1' + '22'

while '211' in z or '112' in z:
	z = z.replace('11', '1', 1)
	if '21' in z:
		z = z.replace('21', '12', 1)
	else:
		z = z.replace('12', '1', 1)
print(z)
f = open('24-s1.txt')
k = 0
for s in f:
	for i in range(1, len(s)-2):
		if s[i-1] == "Z" and s[i+1] == "R" and s[i+2] == "O":
			k+=1
print(k)
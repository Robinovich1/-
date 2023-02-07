a = []
for i in range(0,50):
  for j in range(0,50):
    for k in range(0,50):
      if (1*i + 2*j + 3*k == 56 and
          1*i + 1*j + 3*k == 44 and
          0*i + 1*j + 1*k == 19):
        a.append(i+j+k)
print( min(a) )

#s ='030'
#while not '00' in s:
#    s = s.replace('01', '21022', 1)
#    s = s.replace('02', '310', 1)
#    s = s.replace('03', '230112', 1)
#print(s.count('1'), s.count('2'), s.count('3'))
for i in range(0,100):
  for j in range(0,100):
    for k in range(0,100):
      if (3*i + 1*j + 7*k == 104 and
          1*i + 0*j + 3*k == 39 and
          2*i + 1*j + 6*k == 83):
        print(i+j+k)


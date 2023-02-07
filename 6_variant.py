import turtle as t
k = 40 # масштаб
t.left( 90 ) # развернуть Черепаху "на север"
for i in range(11):
    t.left( 60)
    t.forward( 4*k )
    

t.up()
for x in range(-10, 10):
  for y in range(-10, 10):
    t.goto( x*k, y*k )
    t.dot( 3 )

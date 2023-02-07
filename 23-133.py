def f(x,y):
    if x < y  : return 0
    if x == y : return 1
    if x >= 0b1000 :
        return f(x - 1,y) + f(0b1000, y)
    if x < 0b1000 :
        return f(x - 1,y) + f(0b100, y)


print(f(0b1100,0b100))
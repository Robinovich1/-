for A in range(1, 500):
    k = 0
    for x in range(1, 1000):
        if ((x % 13 == 0) <= (x % 21 != 0)) or (x + A >= 500):
            k += 1
    if k == 999:
        print(A)
        break
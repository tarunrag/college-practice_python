v = 2
while v <= 10:
    print("TABLES FROM 2 to 10\n")
    print("Multiplication Table of", v)
    c = 1
    while c <= 20:
        print(v, '*', c, '=', v*c)
        c = c+1
    print()
    if v < 10:
        input('press ENTER to continue...')
        print()
    v = v+1

    


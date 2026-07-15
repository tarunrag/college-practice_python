    while True:
    print("FIND LARGEST OF N VALUES\n")

    n = int(input("Number of values: "))
    print()

    c = 1
    while c <= n:
        v = eval(input("Value %d: " % c))
        if c == 1:
            lg = v
        if v > lg:
            lg = v
        c = c + 1

    print()
    print("Largest:", lg, '\n')

    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')

    

while True:
    print("LARGEST AND SMALLEST OF N VALUES\n")

    n = int(input("Enter number of values: "))
    print()

    c = 1
    while c <= n:
        v = eval(input("Value"+str(c)+":"))
        if c == 1: lg = sm = v
        if v > lg: lg = v
        if v < sm: sm = v
        c = c + 1

    print()
    print("Largest :", lg)
    print("Smallest:", sm, '\n')

    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch!= 'y':
        break
    print('\n')

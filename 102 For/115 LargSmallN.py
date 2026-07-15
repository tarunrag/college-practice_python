while True:
    print("INPUT N VALUES AND FIND LARGEST AND SMALLEST WITH REPEAT\n")

    n = int(input("Enter number of values: "))
    print()
    
    for c in range(1, n+1):
        v = eval(input("Value"+str(c)+": "))
        if c == 1: lg = sm = v
        if v > lg: lg = v
        if v < sm: sm = v
    print()
    print("Largest :", lg)
    print("Smallest:", sm, '\n')

    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')

        

while True:

    print("PRIME NUMBERS UPTO N\n")

    n = int(input("Enter limit: "))
    print()

    v = 2
    while v <= n:
        c = 2
        while c < v:
            if v%c == 0:
                break
            c = c + 1
        else:
            print(v, end = ' ')
        v = v + 1
    print('\n')
    
    ch = input("Check another(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')
    

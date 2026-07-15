while True:

    print("FINDING NUMBER OF DIGITS\n")

    v = int(input("Input integer: "))
    print()

    v = abs(v)
    if v == 0:
        c = 1
    else:
        c = 0
        while v:    # while v != 0:
            c = c+1
            v = v//10

    print("Number of digits:", c, '\n')

    ch = input("Check another(Y/N): ")
    if ch != 'Y' and ch!= 'y':
        break
    print('\n')
    
        
        
    

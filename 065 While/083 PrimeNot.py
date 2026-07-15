while True:
    
    print("PRIME OR NOT\n")

    v = int(input("Enter an integer value: "))
    print()

    v = abs(v)
    if v == 0 or v == 1:
        print("Neither prime nor composite")
    else:
        c = 2
        while c < v:
            if v%c == 0:
                print("Not a prime number !")
                break
            c = c + 1
        else:
            print("Prime number !")

    print()
    ch = input("Check another(y/n): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')    
    
    

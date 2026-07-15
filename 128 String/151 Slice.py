while True:
    print("SLICING\n")

    st = input("Enter string: ")
    print()

    while True:
        print("String Entered:", st)
        ln = str(len(st))
        a = int(input("Start  [-"+ln+" to "+ln+"]: "))
        b = int(input("Stop   [-"+ln+" to "+ln+"]: "))
        c = int(input("Step (Default 1): "))
        print()

        print("Sliced string   :", st[a:b:c], '\n')

        if input("Check another(y/n): ").lower() != 'y':
            break
        print('\n')
    print()
    if input("Check another string(y/n): ").lower() != 'y':
        break
    print('\n')

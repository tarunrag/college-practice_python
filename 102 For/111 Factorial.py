while True:
    print("FACTORIAL OF A NUMBER\n")

    v = int(input("Enter an Integer value: "))
    print()

    f = 1
    for c in range(2, v+1):
        f *= c
    print("Factorial =", f)
    
    print()
    ch = input("Do you want to continue? (y/n): ")
    print()

    if ch != 'Y' and ch != 'y':
        break
    print('\n')

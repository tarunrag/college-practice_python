while True:
    print("FACTORIALS OF A NUMBER\n")

    v = int(input("Enter value: "))
    print()

    f = 1
    c = 2
    while c <= v:
        f = f*c
        c = c + 1
    print("Factorial =", f)
    
    print()
    ch = input("Do you want to continue? (y/n): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')


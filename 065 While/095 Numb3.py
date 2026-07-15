while True:
    print("NUMBER PATTERN 2\n")

    n = int(input("Enter number of lines: "))
    print()

    r = 1
    while r <= n:
        c = 1
        while c <= n-r:
            print(end = '  ')
            c = c + 1
        c = r
        while c >= 1:
            print(c, end = ' ')
            c = c - 1
        c = 2
        while c <= r:
            print(c, end = ' ' )
            c = c + 1    
        print()
        r = r + 1

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')
    

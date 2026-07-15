while True:
    print("STAR PATTERN 2\n")

    n = int(input("No. lines to print: "))
    print()

    r = 1
    while r <= n:
        c = 1
        while c <= n-r:
            print(end = ' ')
            c = c + 1
        c = 1
        while c <= r:
            print('*', end = ' ')
            c = c + 1
        print()
        r = r + 1

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')
        
        

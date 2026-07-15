while True:
    print('ALPHABETIC PATTERN - 3\n')

    n = int(input("Number of lines: "))
    print()

    for r in range(1, n+1):
        for c in range(1, n-r+1):
            print(end = '  ')
        for c in range(r, 0, -1):
            print(chr(64+c), end = ' ')
        for c in range(2, r+1):
            print(chr(64+c), end = ' ')
        print()

    for r in range(n):
        for c in range(n-r-1):
            print(end = '  ')
        for c in range(r+1, 0, -1):
            print(chr(64+c), end = ' ')
        for c in range(2, r+2):
            print(chr(64+c), end = ' ')
        print()


    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'y' and ch != 'Y':
        break

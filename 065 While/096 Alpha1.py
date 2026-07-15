while True:
    print('ALPHABETIC PATTERN 1\n')

    n = int(input("Enter number of lines to print: "))
    print()

    r = 1
    while r <=n:
        c = 1
        while c <= r:
            print(chr(64+c), end = ' ')
            c = c + 1
        print()
        r = r + 1

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
        print('\n')

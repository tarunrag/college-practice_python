while True:
    print("SPECIAL PATTERN 1\n")

    n = int(input("Number of lines: "))
    print()

    a = 2*n-1
    for r in range(1, n+1):
        for c in range(1, r):
            print(end = '  ')
        for c in range(1, a+1):
            print('&', end = ' ')
        a -= 2
        print()

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')

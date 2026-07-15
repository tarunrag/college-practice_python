while True:
    print("NUMBER PATTERN - 2\n")

    n = int(input("Number of lines: "))
    print()

    for r in range(1, n+1):
        for c in range(1, n-r+1):
            print(end = '  ')
        for c in range(r, 0, -1):
            print(c, end = ' ')
        print()
        

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    
    

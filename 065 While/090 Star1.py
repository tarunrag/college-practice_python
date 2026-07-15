while True:
    print("STAR PATTERN 1\n")

    n = int(input("No: of lines to print: "))
    print()

    r = 1
    while r <= n:
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
    
    


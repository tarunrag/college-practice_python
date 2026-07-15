while True:
    print("PATTERN 2\n")

    st = input("Enter string: ")
    print()

    n = len(st)
    for c in range(1, n+1):
        print(' '*(n-c) + st[:c])
        
    print()
    if input("Continue?(Y/N): ").lower() != 'y':
        break
    print('\n')
        

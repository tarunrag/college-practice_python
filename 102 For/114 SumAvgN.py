while True:
    print("INPUT N VALUES AND FIND SUM AND AVERAGE\n")

    n = int(input("Enter number of values: "))
    print()
    
    s = 0 
    for c in range(n):
        v = int(input("Value %d: " % (c+1)))
        s += v
    print()
    print("Sum    :", s)
    print("Average:", s/n)

    print()
    ch = input("Continue?(Y/N): ")
    
    if ch != 'Y' and ch != 'y':
        break
    print('\n')
    

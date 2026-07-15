while True:
    
    print("REVERSING AN INTEGER\n")

    v = int(input("Enter integer: "))
    print()

    r = 0
    t = abs(v)
    while t:
        r = r*10 + t%10
        t = t//10
    if v < 0:
        r = -r

    print("Reversed value:", r, '\n')
    
    ch = input("Do you want to continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')
        

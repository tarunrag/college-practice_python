while True:
    print("INPUT N ELEMENTS IN LIST\n")

    n = int(input("Enter value for N: "))
    print()
    
    ls = []
    print("Enter", n, "values...\n")
    for c in range(n):
        v = eval(input('Value '+ str(c+1) +': '))
        ls += [v]
    print()
    
    print("Full List...")
    for v in ls:
        print(v, end = ' ')
    print('\n')

    print("Prime No.s in List...")
    for v in ls:
        for c in range(2, int(v)//2+1):
            if v%c == 0:
                break
        else:
            if v != 0 and v != 1:
                print(v, end = ' ')
    print('\n')

    if input("Check again(Y/N): ").lower() != 'y':
        break
    print('\n')
    
            
            
            

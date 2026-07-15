while True:
    print("ODD AND EVEN VALUES IN LIST\n")

    lst = eval(input("Enter elements for list within []: "))
    print()
    
    le = []
    lo = []
    for v in lst:
        if v%2 == 0:
            le += [v]
        else:
            lo += [v]

    print("Even List:", le)
    print("Odd List :", lo, '\n')
    
    if input("Check again(y/n):").lower() != 'y':
        break
    print('\n')
            

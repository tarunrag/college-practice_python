while True:
    print("FIND SUM AND AVERAGE OF N VALUES\n")

    n = int(input("Enter number of values: "))
    print()
   
    print("Enter values...")
    s = 0
    c = 1
    while c <= n:
        v = eval(input("Value "+str(c)+": "))
        s = s + v
        c = c + 1
    av = s/n
    print()
    print("Sum    :", s)
    print("Average:", av)
        
    print()
    ch = input("Continue? (Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')
    
            
            
            


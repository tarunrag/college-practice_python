while True:
    print("PRINTING MULTIPLICATION TABLE REPEATEDLY\n")

    v = int(input("Enter number of which table you would like to print :"))
    n = int(input("Enter limit :"))
    print()

    for c in range(1, n+1):
            print(v, '*', c, '=', v*c)
    print()
    
    ch = input("Do you want to continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')
        
    

    

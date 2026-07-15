while True:
    print("PRIME NUMBER UPTO N WITH REPEAT\n")

    n = int(input("Enter limit: "))
    print()
    
    for v in range(2, n+1):
       for c in range(2, v):
           if v%c == 0:
               break
       else:
            print(v, end = ' ')
    print('\n')

    ch = input("Continue?(Y/N): ")
    print()

    if ch != 'Y' and ch != 'y':
        break
    print('\n')


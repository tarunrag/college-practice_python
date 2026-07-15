while True:
    print("SUM SERIES : 1^2 + 3^2 + 5^2 till n^2\n")

    n = int(input("Enter number of terms: "))
    print()

    s = 0
    v = 1
    for c in range(1, n+1):
        s += v**2
        v += 2
    print('Sum is :', s, '\n')
    
    s = 0
    v = 1
    for c in range(1, n+1):
        print(str(v) + '^2', end = '')
        if c < n:
            print(end = ' + ')
        s += v**2
        v += 2
    print(' =',  s, '\n')

    ch = input("Continue?(Y/N): ")
    if ch != 'Y' or ch != 'y':
        break
    print("\n")
    
        

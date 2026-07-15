while True:
    print('Series - (2/9 - 5/13 + 8/17 till n with repeat\n')

    n = int(input("Enter number of terms: "))
    print()
    s = 0
    nu = 2
    de = 9
    for c in range(n):
        if c%2 != 0:
            s -= nu/de
        else:
            s += nu/de
        nu += 3
        de += 4
    print("Sum of Series:", s)

    ch = input("Continue?(Y/N): ")
    if ch != 'Y' or ch != 'y':
        break
        

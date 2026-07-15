while True:
    print("1 + 1/1! + 1/2! + 1/3! .... 1/n!\n")

    n = int(input("Enter limit: "))
    print()
    s = 1
    f = 1
    v = 1
    for c in range(n):
        f *= v
        s += 1/f
        v += 1
    print("Sum of series:", s, '\n')
    

    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')

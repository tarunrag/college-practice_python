while True:
    print('COUNT OF WORDS\n')

    st = input("String: ")
    print()

    c = 0
    for ch in st:
        c += 1
    print("Count of words is :", c)
    
    ln = len(st)-1
    wd = 0
    for c in range(ln):
        if st[c] != ' ' and (st[c+1]== ' ' or c+1 == ln):
            wd += 1
    
    print("Count of words is:", wd)

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')

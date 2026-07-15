while True:
    print("CHARACTER COUNT\n")

    st = input("String: ")
    print()

    u = l = s = c = 0
    for ch in st:
        if ch >= 'A' and ch <= 'Z':
            u += 1
        if ch >= 'a' and ch <= 'z':
            l += 1
        if ch == ' ':
            s += 1
        c += 1
    print()

    print('Upper Case Alphabets =', u)
    print('Lower Case Alphabets =', l)
    print('Spaces =', s)
    print('Total No. of Characters :', c)

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'y' and ch != 'Y':
        break
    print('\n')

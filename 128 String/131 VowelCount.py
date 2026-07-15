while True:
    print('VOWEL COUNT\n')

    st = input("String: ")
    print()

    a = e = i = o = u = 0
    for ch in st:
        if ch in 'Aa':
            a += 1
        if ch in 'Ee':
            e += 1
        if ch in 'Ii':
            i += 1
        if ch in 'Oo':
            o += 1
        if ch in 'Uu':
            u += 1
    v = a + e + i + o + u
    
    print("A's =", a)
    print("E's =", e)
    print("I's =", i)
    print("O's =", o)
    print("U's =", u)
    print("Total Vowel Count:", v)

    print()
    ch = input("Check more?..(Y/N): ")
    if ch != 'y' and ch != 'Y':
        break
    print('\n')

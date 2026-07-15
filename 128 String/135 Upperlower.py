while True:
    print("STRING TO UPPER & LOWER CASE\n")

    st = input("Enter string: ")
    print()

    uc = lc = ''
    for ch in st:
        if ch >= 'A' and ch <= 'Z':
            lc += chr(ord(ch)+32)
        else:
            lc += ch
        if ch >= 'a' and ch <= 'z':
            uc += chr(ord(ch)-32)
        else:
            uc += ch 
    print("In Upper case:", uc)
    print("In Lower case:", lc)

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')

    

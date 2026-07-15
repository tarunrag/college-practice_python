while True:
    print("CONCATENATION OF STRINGS\n")

    st1 = input("Enter First string : ")
    st2 = input("Enter Second string: ")
    print()

    st3 = ''
    for ch in st1:
        st3 += ch
    st3 += ' '
    for ch in st2:
        st3 += ch
    print("Concatenated string:", st3)
    print("Concatenated String:", st1 + ' ' + st2)
    
    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')

    


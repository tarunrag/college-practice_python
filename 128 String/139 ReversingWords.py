while True:
    print("REVERSING WORDS IN A SENTENCE\n")

    st = input("Enter string: ")
    print()

    rs = wd = '' 
    for ch in st:
        if ch != ' ':
            wd = ch + wd
        else:
            rs += wd + ' '
            wd = ''
    rs += wd        

    print("Reversed string:", rs)
    
    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'y' and ch != 'Y':
        break
    print('\n')
    

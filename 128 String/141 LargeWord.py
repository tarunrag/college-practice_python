while True:
    print("LARGEST WORD IN STRING\n")

    st = input("Enter a string: ")
    print()
    
    wd = ''
    lg = 0
    for ch in st:
        if ch != ' ':
            wd = wd + ch
        else:
            if len(wd) > lg:
                lg = len(wd)
                lw = wd
            wd = ''
    if len(wd)>lg:
        lw = wd  
    print("Largest word:", lw)

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'y' and ch != 'Y':
        break
    print('\n')
    
        

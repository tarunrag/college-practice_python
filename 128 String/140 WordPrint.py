while True:
    print("WORD STARTING WITH THE GIVEN LETTER\n")

    st = input("Enter a string: ")
    le = input("Enter a letter: ")
    print()
    
    print("Words starting with letter '"+le+"'")
    wd = ''
    for ch in st:
        if ch != ' ':
            wd += ch 
        else:
            if wd[0] == le:
                print(wd)
            wd = ''
        
     
    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'y' and ch != 'Y':
        break
    print('\n')
    
            
        

while True:
    print('SALUTATION\n')

    na = input("Name       : ")
    ge = input("Gender(M/F): ")
    #if ge == 'M' or ge == 'm':
    if ge in 'Mm':
        print()
        print('Hello Mr.', na)
    #elif ge == 'F' or ge == 'f':
    elif ge in 'Ff':
        mt = input('Marital Status(M/U): ')
        print()
        #if mt == 'M' or mt == 'm':
        if mt in 'Mm':
            print('Hello Mrs.', na)
        #elif mt == 'U' or mt == 'u':
        elif mt in 'Uu':
            print('Hello Miss.', na)
        else:
            print('Invalid Marital Status Code !')
    else:
        print('Invalid Gender Code !')

    print()
    ch = input("Check more?..(Y/N): ")
    if ch != 'y' and ch != 'Y':
        break
    print('\n')


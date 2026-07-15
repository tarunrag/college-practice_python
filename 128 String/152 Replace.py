while True:
    print("REPLACING\n")

    st = input("Enter string: ")
    print()

    while True:
        sb = input("Enter substring to replace     : ")
        sr = input("Enter substring to replace with: ")
        print()

        print("After replacing: ", st.replace(sb, sr))
        print('\n')

        if input("Check again(y/n): ").lower() != 'y':
            break
        print('\n')

    print()

    if input("Check another string(y/n): ").lower() != 'y':
        break
    print('\n')
    

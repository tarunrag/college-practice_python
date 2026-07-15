while True:
    print("SEARCHING\n")
    
    st = input("Enter string: ")
    print()
    while True:
        sb = input("Enter substring: ")
        id = 0
        while True:
            id = st.find(sb, id)
            if id == -1:
                print("Not found !")
                break
            else:
                print("Found at index:", id)
                id += 1
            if input("Continue Search(Y/N): ").lower() != 'y':
                break
            print('\n')
        print()
        if input("Check another substring(Y/N): ").lower() != 'y':
            break
        print('\n')
    print()
    if input("Check again(Y/N): ").lower() != 'y':
        break
    print('\n')
    

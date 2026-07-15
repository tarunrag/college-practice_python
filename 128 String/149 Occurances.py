while True:
    print("NUMBER OF OCCURENCES OF SUBSTRING\n")

    st = input("Enter the string: ")
    print()

    while True:
        sb = input("Enter Substring to Search: ")
        print()

        print("No. of Occurences:", st.count(sb), '\n')

        if input("Check another Substring: ").lower() != 'y':
            break
        print('\n')

    print()

    if input("Repeat(Y/N): ").lower() != 'y':
        break
    print('\n')

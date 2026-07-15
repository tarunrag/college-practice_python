while True:
    print("STRING FUNCTIONS\n")

    st = input("Enter string: ")
    print()

    print("String Length:", len(st))
    print("Lowercase :", st.lower())
    print("Uppercase :", st.upper())
    print("Titlecase :", st.title())
    print("Captialize:", st.capitalize())
    print("Swapcase  :", st.swapcase())

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'y' and ch != 'Y':
         break
    print('\n')

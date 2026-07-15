while True:
    print("TRIMING SPACES\n")

    st = input("Enter the string: ")
    print()

    print("String: ["+ st + ']')
    print("lstrip: [" + st.lstrip() + ']')
    print("rstrip: ["+ st.rstrip() + ']')
    print("strip : ["+ st.strip() + ']')

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'y' and ch != 'Y':
        break
    print('\n')
    

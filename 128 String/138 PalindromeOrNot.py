while True:
    print("PALINDROME OR NOT\n")

    st = input("Enter string: ")
    print()

    re = ''
    for ch in st:
        re = ch + re
    if st == re:
         print("It's a palindrome !")
    else:
        print("It's NOT a palindrome !")
    
    if st == st[::-1]:
        print("It's a palindrome !")
    else:
        print("It's NOT a palindrome !")

    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'y' and ch != 'Y':
        break
    print('\n')

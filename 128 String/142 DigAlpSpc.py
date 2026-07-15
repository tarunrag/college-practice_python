while True:
    print("DIGIT, ALPHABET OR SPECIAL CHARACTER\n")

    ch = input("Enter a character: ")
    print()

    if ch.isdigit():
        print("It's a digit")
    elif ch.isalpha():
        print("It's an Alphabet")
        if ch.isupper():
            print("It's in Upper case")
        elif ch.islower():
            print("It's in Lower case")
        else:
            print("It's in Mixed case")
    elif ch.isspace():
        print("It is a white space")
    else:
        print("It is a special character")

    print()
    co = input("Continue?(Y/N): ")
    if co != 'y' and co != 'Y':
        break
    print('\n')


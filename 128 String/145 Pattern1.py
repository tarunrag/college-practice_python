while True:
    print("PATTERN 1\n")

    st = input("Enter the string: ")
    print()

    for c in range(len(st), 0, -1):
        print(st[:c])

    print()
    if input("Continue(Y/N): ").lower() != 'y':
        break
    print('\n')
        

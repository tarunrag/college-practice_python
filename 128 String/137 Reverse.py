while True:
    print("REVERSING STRING\n")

    st = input("Enter string: ")
    print()

    re = ''
    for ch in st:
        re = ch + re
    print("Reversed string: ", re)   

    print("Reversed string: ", st[::-1])
    
    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')
        

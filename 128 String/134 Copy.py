while True:
    print('COPYING STRING\n')

    st = input('Enter a string: ')
    print()
    
    cs = ''
    for ch in st:
        cs += ch
    print("Copied String:", cs)

    cs = st
    print("Copied String:", cs)
    
    print()
    ch = input("Continue?(Y/N): ")
    if ch != 'y' and ch != 'Y':
        break
    print('\n')

    

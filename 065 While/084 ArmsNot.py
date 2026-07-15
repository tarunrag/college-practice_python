while True:
    print("ARMSTRONG NUMBER OR NOT\n")

    v = int(input('Enter an integer: '))
    print()

    c = 0
    t = v
    while t:
        c = c + 1
        t = t//10

    a = 0
    t = v
    while t:
        a = a + (t%10)**c
        t = t//10

    if a == v:
        print("Armstrong number !")
    else:
        print('Not armstrong number !')

    print()
    ch = input("Check another(Y/N): ")
    if ch != 'Y' and ch != 'y':
        break
    print('\n')
    
        

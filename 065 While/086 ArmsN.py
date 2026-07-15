while True:
    
    print("ARMSTRONG NUMBERS UPTO N\n")

    n = int(input("Enter limit :"))
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


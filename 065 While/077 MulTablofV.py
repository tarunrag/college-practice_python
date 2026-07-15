while True:
    print("MULTIPLICATION TABLE OF INPUT VALUE\n")

    v = eval(input("Enter value: "))
    n = eval(input("Enter Limit: "))
    print()

    c = 1
    while c <= n:
        print(v, '*', c, '=', v*c)
        c = c + 1

    print()
    ch = input("Try again (y/n) ?: ")
        
    #if ch not in 'Yy':    (DONT USE WILL NOT WORK FOR ENTER SPACE AND WILL BE CONSIDERED AS YES!!!)
        break
    print('\n')
        
    
    

while True:
    print("x - x^2/2! + x^3/3! - x^4/4! .... till x^n/n!\n")

    x = eval(input("Enter value for x: "))
    n =  int(input("Enter value for n: "))
    print()
    
    s = x
    f = 1   
    for c in range(2, n+1):
        f *= c
        if c%2 != 0:
            s += (x**c)/f
        else:
            s -= (x**c)/f
    print("Sum of series:", s, '\n')
    

    ch = input("Continue?(Y/N): ")
    if ch != 'y' and ch != 'Y':
        break
    print('\n')
        

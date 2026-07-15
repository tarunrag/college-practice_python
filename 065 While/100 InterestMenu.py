mn = '''
INTEREST CALCULATION – Menu Driven

1. Simple Interest
2. Compound Interest
3. Exit Program

Enter choice(1-3): '''

while True:
    ch = input(mn)
    print()

    if ch == '1':
        p =  int(input("Principal amount: "))
        y =  int(input("Number of Years : "))
        r =  eval(input("Interest Rate   : "))
        print()
        s = p*y*r/100    
        print("Simple Interest is:", round(s, 2))
        
    elif ch == '2':
        p =  int(input("Principal amount: "))
        y =  int(input("Number of Years : "))
        r =  eval(input("Interest Rate   : "))
        print()
        a = p*(1+r/100)**y-p
        print("Compound Interest is:", round(a, 2))
        
    elif ch == '3':
        break
    
    else:
        print("Invalid Choice")
    print('\n')
    
        
    
        
    

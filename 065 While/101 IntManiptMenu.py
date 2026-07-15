mn = '''INTEGER MANIPULATIONS - MENU DRIVEN
1.Sum of Digits
2.Number of Digits
3.Reversing
4.Exit Program\n
Enter Choice: '''

while True: 
    ch = input(mn)
    print()
    
    n = int(input("Enter number: "))
    print()
    
    if ch == '1':
        s = 0 
        while n != 0:
            s = s+n%10
            n = n//10
        print("Sum of Digits is:", s)
        
    elif ch == '2':
        c = 0
        while c < len(str(n)):
            c = c + 1
        print("Number of Digits is:", c)

    elif ch == '3':
        print("Reversed number is:", str(n)[::-1])
        
    elif ch == '4':
        break
    else:
        print("Invalid choice !")
    print('\n')
        
    
            
    



mn = '''
TEMPERATURE CONVERSION – Menu Driven

1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter choice: '''

while True:
    ch = int(input(mn))
    print()

    if ch==1:
        c = eval(input("Enter temperature in celcius: "))
        print('Corresponding Fahrenheit Temperature is:', 1.8*c+32)
    elif ch == 2:
        f = eval(input("Enter temperature in fahrenheit: "))
        print('Corresponding Celcius Temperature is:', (f-32)/1.8)
    else:
        print('invalid choice')
    print('\n')

    ca = input("Check again?(y/n): ")
    if ca != 'Y' and ca != 'y':
        break
    print('\n')
    

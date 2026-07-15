print("TEMPERATURE CONVERSION\n")

ch = input("enter unit of temperature to convert to(C/F): ")
print()

if ch in 'Cc':
    f = eval(input("Enter temperature in Fahrenheit: "))
    print("Corresponding Celcius Temperature is:", (f-32)/1.8)
elif ch in 'Ff' :
    c = eval(input("Enter temperature in Celcius: "))
    print("Corresponding Fahrenheit Temperature is:", 1.8*c+32)
else:
    print("Invalid Unit entered !")    
    
     

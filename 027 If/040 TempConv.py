print("TEMPERATURE CONVERSION\n")

u = input("Enter Unit to convert to (Celcius/Fahrenheit (C/F)): ")
print()

if u == 'C' or u == 'c':
    f = eval(input("Enter temperature in Fahrenheit: "))
    print("Corresponding Celcius Temperature is:", (f-32)/1.8)
   
if u == 'F' or u == 'f':
    c = eval(input("Enter temperature in Celcius: "))
    print("Corresponding Fahrenheit Temperature is:", 1.8*c+32)

if u != 'C' and u != 'c' and u != 'F' and u != 'f':
    print("Invalid Unit entered")
    

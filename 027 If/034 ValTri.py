print("VALID TRIANGLE OR NOT\n")

print("Enter three sides of a Triangle...")
a = eval(input("Side 1: "))
b = eval(input("Side 2: "))
c = eval(input("Side 3: "))
print()

if a+b > c and b+c > a and a+c > b:
    print("Valid Triangle !")

if a+b <= c or b+c <= a or a+c <= b:  
    print("Invalid Triangle !")

print("EVEN NUMBERS FROM A TO B AND COUNT\n")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = 0 
print()

if a == b:
    if a%2 != 0:
        print("No values to print")
    else:
        print(a)
        c = 1
        
elif a < b:
    if a%2 != 0:
        a += 1
    for v in range(a, b+1, 2):
        print(v, end = "\t")
        c += 1
else:
    if a%2 != 0:
        a -= 1
    for v in range(a, b-1, -2):
        print(v, end = "\t")        
        c += 1
        
print()
print("Count is:", c)
        
        
        
        

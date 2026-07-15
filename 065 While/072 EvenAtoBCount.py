print("EVEN VALUE(S) BETWEEN A & B\n")

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = 0
print()

print("Values between", a, "&", b, "are ...")
if a == b:
    if a%2 != 0:
        print("No values to print")
    else:
        print(a)
        c = 1
        
elif a < b:
    if a%2 != 0:
        a = a + 1
    while a <= b:
        print(a, end = "\t")
        c = c + 1
        a = a + 2
else:
    if a%2 != 0:
        a = a  - 1
    while a >= b:
        print(a, end = "\t")        
        c = c + 1
        a = a - 2
print()
print("Count =", c)

        
    

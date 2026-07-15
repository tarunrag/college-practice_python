print("ODD VALUE(S) BETWEEN A & B\n")

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
print()

print("Values between", a, "&", b, "are ... ")
if a == b:
    if a%2==0:
        print("No values to print")
    else:
        print(a)
elif a%2 == 0:
    a = a + 1
    while a <= b:
        print(a, end = "\t")
        a = a + 2
else:
    while a <= b:
        print(a, end = "\t")
        a = a + 2
        

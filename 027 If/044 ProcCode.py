print("FIND RESULT\n")

a = eval(input("Enter Value 1 : "))
b = eval(input("Enter Value 2 : "))
print("""Operation to perform...
1.  Add
2.  Subtract
3.  Multiply
4.  Divide
5.  Remainder""")
pc = int(input("Enter Process Code (1-5): "))
print()

if pc >= 1 and pc <= 5:
    if pc == 1:
        rs = a+b
    if pc == 2:
        rs = a-b
    if pc == 3:
        rs = a*b
    if pc == 4:
        if b != 0:
            rs = a/b
        if b == 0:
            rs = "undefined"
    if pc == 5:
        if b != 0:
            rs = a%b
        if b == 0:
            rs = "undefined"
    print("Result:", rs)
    
if pc < 1 or pc > 5:
    print("Invalid Process Code !")
    
    

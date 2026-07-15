print("FIND RESULT\n")

a = eval(input("Enter Value 1 : "))
b = eval(input("Enter Value 2 : "))
op = input("Enter Arithmetic operator(+ - * / % // **): ")
print()

if op in '+-*/%//**':
    if op == '+':
        rs = a+b
    elif op == '-':
        rs = a-b
    elif op =='*':
        rs = a*b
    elif op == '**':
        rs = a**b
    else:
        if b == 0:
            rs = "undefined"
        elif op == '%':
            rs = a%b
        elif op == '/':
            rs = a/b
        else:
            rs = a//b            
    print("Resultant expression:", a, op, b, '=', rs)
else:
    print("Invalid Arithmetic operator !")

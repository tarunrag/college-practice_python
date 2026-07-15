print("FIND RESULT\n")

a = eval(input("Enter Value 1 : "))
b = eval(input("Enter Value 2 : "))
op = input("Enter Arithmetic operator(+ - * / %): ")
print()

if op == '+' or op == '-' or op =='*' or op == '*' or op == '/' or op =='%':
    if op == '+':
        rs = a+b
    if op == '-':
        rs = a-b
    if op =='*':
        rs = a*b
    if op == '/':
        if b != 0:
            rs = a/b
        if b == 0:
            rs = "undefined"
    if  op == '%':
        if b != 0:
            rs = a%b
        if b == 0:
            rs = "undefined"
            
    print("Resultant expression:", a, op, b, '=', rs)
    
if op != '+' and  op != '-' and op !='*' and  op != '*' and op != '/' and op !='%':
    print("Invalid Arithmetic operator !")
    

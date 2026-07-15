print("LARGEST AMONG THREE VALUES\n")

v1 = eval(input("First Value : "))
v2 = eval(input("Second Value: "))
v3 = eval(input("Third Value : "))
print()

if v1 > v2:
    if v1 > v3:
        lg = v1
    else:
        lg = v3
else:
    if v2 > v3:
        lg = v2
    else:
        lg = v3
        
print("Largest value is:", lg)

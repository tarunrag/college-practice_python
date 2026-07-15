print("LARGEST AMONG THREE VALUES\n")

v1 = eval(input("First Value : "))
v2 = eval(input("Second Value: "))
v3 = eval(input("Third Value : "))
print()

##if v1 > v2 > v3 or v1 > v3 > v2 or  v1 == v2 > v3 or v1 == v3 > v2 or v1 > v2 == v3 :
##    print("Largest:", v1)
##if v2 > v1 > v3 or v2 > v3 > v1  or v2 == v3 > v1 or v2 > v1 == v3 :
##    print("Largest:", v2)
##if v3 > v1 > v2 or v3 > v2 > v1  or v3 == v1 > v2 or v3 > v1 == v2 :
##    print("Largest:", v3)
##if v1 == v2 == v3:
##    print("Largest:", v1)

if v1 > v2:
    if v1 > v3:
        lg = v1
    if v1 <= v3:
        lg = v3
if v1 <= v2:
    if v2 > v3:
        lg = v2
    if v2 <= v3:
        lg = v3

print("Largest:", lg)
    

    print("SORTING A, B, C\n")

a = eval(input("First value : "))
b = eval(input("Second value: "))
c = eval(input("Third value : "))
print()

print("Sorted Order:", end =" ")
if a < b:
    if a < c:
        if b < c:
            print(a, b, c)
        if b >= c:
            print(a, c, b)
    if a >= c:
        print(c, a, b)
if a >= b:
    if b < c:
        if a < c:
            print(b, a, c)
        if a >= c:
            print(b, c, a)
    if b >= c:
        print(c, b, a)
        
print()
print("Sorted Order:", sorted([a, b, c]))

    




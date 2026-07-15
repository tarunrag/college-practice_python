print("VALUE & FACTORIAL VALUES UPTO N\n")

n = int(input("Enter value for N: "))
print()

print("Value ", "Factorial",  sep = "\t")
v = 1
f = 1
while v <= n:
    f = f*v
    print(v, f, sep = "      \t")
    v = v + 1
    

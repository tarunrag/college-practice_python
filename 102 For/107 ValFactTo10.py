print("VALUE & FACTORIAL UPTO 10 IN TABULAR FORM\n")

n = int(input("Enter value for N: "))
print()

print("Value ", "Factorial",  sep = "\t")
v = 1
f = 1
for i in range (v, n+1, 1):
    f = f*v
    print(v, f, sep = "     \t")
    v = v + 1

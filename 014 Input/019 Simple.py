print("CALCULATION OF SIMPLE INTEREST\n")

p =  int(input("Principal amount: "))
y =  int(input("Number of Years : "))
r = eval(input("Interest Rate   : "))
print()

s = p*y*r/100

print("Simple Interest is:", str(s) + '/- Rs.')

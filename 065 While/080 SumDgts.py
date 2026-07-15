print("SUM OF DIGITS \n")

v = int(input("enter integer value: "))
print()

s = 0
while v != 0:
    s = s+v%10
    v = v//10
print("Sum of digits is:", s)

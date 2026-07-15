print("SWAPPING\n")

a = eval(input("Enter first Value : "))
b = eval(input("Enter Second Value: "))
print()

##t = a   # using third variable
##a = b
##b = t

##a = a+b     #without the use of third variable 
##b = a-b
##a = a-b

a, b = b, a     #only in python 

print("Values after swapping......")
print("First Value :", a)
print("Second Value:", b)

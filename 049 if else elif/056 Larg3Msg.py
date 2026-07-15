print("LARGEST OF THREE MESSAGES\n")

v1 = eval(input("First Value : "))
v2 = eval(input("Second Value: "))
v3 = eval(input("Third Value : "))
print()

if v1 == v2 and v2 == v3:
    print("All values are Equal !")         
elif v1 > v2 and v1 > v3:                     
    print("First Value Largest !")
elif v2 > v1 and v2 > v3:
    print("Second Value Largest !")
elif v3 > v1 and v3 > v2:
    print("Third Value Largest !")
elif v1 == v2 and v1 > v3:
    print("First and Second Equal and Larger than Third !")
elif v2 == v3  and v2 > v1:
    print("Second and Third Equal and Larger than First !")
else:
    print("First and Third Equal and Larger than Second !")
        

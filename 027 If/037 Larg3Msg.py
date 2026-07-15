print("LARGEST AMONG THREE VALUES (MESSAGES)\n")

v1 = eval(input("First Value : "))
v2 = eval(input("Second Value: "))
v3 = eval(input("Third Value : "))
print()

if v1 == v2 and v2 == v3:
    print("All values are Equal !")         #here the question requires us to specifically find which one is greatest.
if v1 > v2 and v1 > v3:                     # in this case when 2 are equal it will go to the statements provided below.
    print("First Value Largest !")
if v2 > v1 and v2 > v3:
    print("Second Value Largest !")
if v3 > v1 and v3 > v2:
    print("Third Value Largest !")
if v1 == v2 and v1 > v3:
    print("First and Second Equal and Larger than Third !")
if v2 == v3  and v2 > v1:
    print("Second and Third Equal and Larger than First !")
if v1 == v3  and v1 > v2:
    print("First and Third Equal and Larger than Second !")

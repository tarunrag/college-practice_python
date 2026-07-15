print("ZERO, EVEN OR ODD VALUE\n")

v = int(input("Enter an Integer value: "))
print()


if v == 0:
    print("Zero !")
if v != 0 and v%2 == 0:
    print("Even !")
if v%2 != 0:
    print("Odd")
    


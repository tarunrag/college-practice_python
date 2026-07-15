print("NUMBER OF DIGITS\n")

v = int(input("Enter a value(Max 5 Digits): "))
print()

if v >= -99999 and v <= 99999:
    if v >= -9 and v <= 9:
        nd = 1
    elif v >= -99 and v <= 99:
        nd = 2
    elif v >= -999 and v <= 999:
        nd = 3
    elif v >= -9999 and v <= 9999:
        nd = 4
    else:
        nd = 5
    print("Number of digits:", nd)
else:
    print("Invalid data (Max 5 Digits) !")
    

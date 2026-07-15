print("LEAP YEAR OR NOT\n")

y = int(input("Enter a Year: "))
print()

if y%4 == 0 and y%400 == 0 or  y%100 != 0:
    print(y, "is a Leap Year !")
else:
    print(y,"is NOT a Leap Year !")
    
    

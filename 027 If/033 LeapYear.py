print("LEAP YEAR OR NOT\n")

y = int(input("Enter a Year: "))
print()

if y%4 == 0 and y%100 != 0 or y%400 == 0:
    print("Leap Year !")
if y%4 != 0 or y%100 == 0 and y%400 != 0:
    print("NOT Leap Year !")

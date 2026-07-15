print("WEEKDAY IN WORDS\n")

w = int(input("Enter Weekday number (1-7): "))
print()

##if w==1:
##    print("Weekday number 1 represents ...... Sunday !")
##if w==2:
##    print("Weekday number 2 represents ...... Monday !")
##if w ==3:
##    print("Weekday number 3 represents ...... Tuesday !")
##if w ==4:
##    print("Weekday number 4 represents ...... Wednesday !")
##if w==5:
##    print("Weekday number 5 represents ...... Thursday !")
##if w==6:
##    print("Weekday number 6 represents ...... Friday !")
##if w>6:
##    print("Weekday number", w, "represents....... Invalid Weekday !")

if w == 1:
    wd = "Sunday"
if w == 2:
    wd = "Monday"
if w == 3:
    wd = "Tuesday"
if w == 4:
    wd = "Wednesday"
if w == 5:
    wd = "Thursday"
if w == 6:
    wd = "Friday"
if w == 7:
    wd = "Saturday"
if w < 1 or w > 7:
    wd = "Invalid Weekday"

print("Weekday number", w, "represents ......", wd, "!")
    

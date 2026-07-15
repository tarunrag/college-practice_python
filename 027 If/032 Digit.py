print("DIGIT IN WORDS\n")

d = int(input("Enter a Digit (0-9): "))
print()

if d == 0:
    dg = "Zero"
if d == 1:
    dg = "One"
if d == 2:
    dg = "Two"
if d == 3:
    dg = "Three"
if d == 4:
    dg = "Four"
if d == 5:
    dg = "Five"
if d == 6:
    dg = "Six"
if d == 7:
    dg = "Seven"
if d == 8:
    dg = "Eight"
if d == 9:
    dg = "Nine"
if d < 0 or d > 9:
    dg = "Invalid Data"

print("Digit", d, "in words is ...", dg)

    
    

print("VOTING ELIGIBILITY\n")

a = int(input("Enter Age of person: "))
print()

if a < 18:
    print("NOT Eligible to Vote !")
if a >= 18:
    print("Eligible to Vote !")

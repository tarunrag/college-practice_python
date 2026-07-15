print("FIND TOTAL, PERCENTAGE & RESULT (BASED ON MARKS)\n")

mm = int(input("Maximum marks in a Subject: "))
pm = int(input("Pass mark in a Subject: "))
print("Enter the three marks scored by the student.....")
m1 = int(input("Mark 1: "))
m2 = int(input("Mark 2: "))
m3 = int(input("Mark 3: "))
print()

tm = m1 + m2 + m3
pr = tm/(mm*3)*100

if m1 >= pm and m2 >= pm and m3 >= pm:
    rs = "Passed"
if m1 < pm or m2 < pm or m3 < pm:
    rs = "Failed"

print("Total Marks:", tm)
print("Percentage :", pr, '%')
print("Result     :", rs)


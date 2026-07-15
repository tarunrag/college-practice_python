print("FIND TOTAL, PERCENTAGE & GRADE\n")

mm = eval(input("Enter Maximum marks: "))
pp = eval(input("Pass Percentage: "))
print("Enter the three marks scored by the student.....")
m1 = eval(input("Mark 1: "))
m2 = eval(input("Mark 2: "))
m3 = eval(input("Mark 3: "))
print()

tm = m1 + m2 + m3
pr = tm/(mm*3)*100
pm = (mm*pp)/100
if m1 < pm or m2 < pm or m3 <pm:
    gr = "F"
if m1 >= pm and m2 >= pm and m3 >= pm:
    if pr < 60:
        gr = "C"
    if pr >= 60 and pr < 70:
        gr = "B"
    if pr >= 70 and pr < 80:
        gr = "B+"
    if pr >= 80 and pr < 90:
        gr = "A"
    if pr >= 90:
        gr = "A+"

print("Total Marks:", tm)
print("Percentage :", pr, '%')
print("Grade      :", gr)


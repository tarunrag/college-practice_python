print("STUDENT'S MARK DETAILS")
print("=======================")

ro, na, cl, dv=23, "shankaran", "XII", "C"
m1, m2, m3, m4, m5, m6 = 99, 95, 98, 94, 93, 100
tt = m1+m2+m3+m4+m5+m6
pr = tt/600*100


print("Roll No. :", ro)
print("Name     :", na)
print("Class    :", cl)
print("Division :", dv, '\n')

print("Marks scored in 6 Subjects...")
print("Mark 1   :", m1) 
print("Mark 2   :", m2)
print("Mark 3   :", m3)
print("Mark 4   :", m4)
print("Mark 5   :", m5)
print("Mark 6   :", m6, '\n')

print("Total Marks:", tt)
print("Percentage :", pr, '%\n')

print("REPORT")
print("------")
print("Rollno", "Name\t", "Class", "Div.", "Total", "Perc.", sep="\t")
print(ro, na, cl, dv, tt, pr, sep="\t")



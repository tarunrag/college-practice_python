print("FIND TOTAL, PERCENTAGE & RESULT (BASED ON PERCENTAGE)\n")

mm = eval(input("Maximum marks in a Subject: "))
pp = eval(input("Pass percentage           : "))
print("Enter the three marks scored by the student...")
m1 = eval(input("Mark 1: "))
m2 = eval(input("Mark 2: "))
m3 = eval(input("Mark 3: "))
print()

tm = m1+m2+m3
pr = tm/(mm*3)*100
if pr < pp:
    rs = "Failed"
if pr >= pp:
    rs = "Passed"
    
print("Total Marks:", tm)
print("Percentage :", pr, '%')
print("Result     :", rs)

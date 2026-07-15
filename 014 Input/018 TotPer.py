print("FIND TOTAL & PERCENTAGE\n")

mx = eval(input("Maxiumum Marks: "))
print("Marks Scored...")
m1 = eval(input("Mark 1: "))
m2 = eval(input("Mark 2: "))
m3 = eval(input("Mark 3: "))
m4 = eval(input("Mark 4: "))
m5 = eval(input("Mark 5: "))
print()

tm = m1+m2+m3+m4+m5
pr = tm/(mx*5)*100

print("Total marks     :", tm )
print("Total percentage:", round(pr, 2), '%')


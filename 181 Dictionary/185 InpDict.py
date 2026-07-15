print("INPUTING & PRINTING DICTIONARY\n")

n = int(input("enter number of students: "))
print()

dc = {}
for c in range(n):
    print("Student", c+1, "...")
    rn = int(input("Rollno: "))
    na =     input("Name  : ")
    dc[rn] = na
    print('\n')
    
print("Students with Odd Rollno.s...\n")
for k in dc:
    if k%2 != 0:
        print(k)

print("Students with Even Rollno.s...\n")
for k in dc.keys():
    if k%2 == 0:
        print(k)
    

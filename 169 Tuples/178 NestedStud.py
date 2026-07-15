print("NESTED TUPLE - STUDENT\n")

##tp = ()
##while True:
##    print("Enter Student Details...")
##    rn = input("Roll no : ")
##    na = input("Name    : ")
##    cl = input("Class   : ")
##    dv = input("Division: ")
##    print()
##    print("Enter 5 Marks scored in Series(Max 100)...")
##    s1 = tuple(eval(input("Series 1: ")))
##    s2 = tuple(eval(input("Series 2: ")))
##    s3 = tuple(eval(input("Series 3: ")))
##    print()
##    
##    tp += (rn, na, cl, dv, (s1, s2, s3)), 
##
##    if input("Input More(y/n): ").lower() != 'y':
##        break
##    print('\n')

tp = (('12', 'tim', '12', 'E', ((99, 98, 97, 96, 95), (99, 98, 97, 96, 94), (100, 88, 75, 44, 68))),
      ('23', 'hanah', '12', 'C', ((99, 98, 97, 96, 95), (98, 95, 94, 93, 92), (50, 56, 78, 99, 89))))
    
print("STUDENTS REPORT")
print("===============\n")

for rn, nm, cl, dv, sr in tp:
    print("%-10s %-15s %-20s %-15s" %
    ("Rollno", "Name", "Class", "Divison", ))
    print("%-10s %-15s %-20s %-15s\n" %
          (rn, nm, cl, dv))
    
    print("%-10s %5s %5s %5s %5s %5s %10s %10s   %5s" %
          ("Series", "m1", "m2", "m3", "m4", "m5", "Total", "Percentage", "Grade"))
    for d in range(3):
        tt = sum(sr[d])
        pr = tt/5
        if min(sr[d]) < 40:
            gr = "F"
        else:
            if pr < 50:
                gr = "D"
            elif pr < 60:
                gr = "C"
            elif pr < 70:
                gr = "B"
            elif pr < 80:
                gr = "B+"
            elif pr < 90:
                gr = "A"
            else:
                gr = "A+"

        print("%-10s %5s %5s %5s %5s %5s %10s %10.2f   %5s" %
          (d+1, sr[d][0], sr[d][1], sr[d][2], sr[d][3], sr[d][4], tt, pr, gr))
    print('-'*80)
        
                    
              
              



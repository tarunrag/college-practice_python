print("INPUTING & PRINTING DICTIONARIES\n")

##dc = {}
##while True:     
##    emp = int(input("Emp No.: "))
##    ena =     input("Name   : ")
##    eba = int(input("Basic  : "))
##    HRA = int(input("HRA    : "))
##    PF  = int(input("PF     : "))
##
##    dc[emp] = (ena, eba, HRA, PF)
##
##    if input("Input more(y/n): ").lower() != 'y':
##        break
##    print('\n')

dc = {123: ('thomas', 5000, 700, 450),
      125: ('tom', 6000, 800, 600),
      300: ('tim', 7800, 650, 850)}

print("Empno.", "Name", "Basic", "HRA", "PF", "Salary", sep = '\t')
ts = c = 0
for emp, (ena, eba, HRA, PF) in dc.items():
    sa = eba + HRA - PF
    print(emp, ena, eba, HRA, PF, sa, sep = '\t')
    if c == 0:
        hs = ls = sa
    if sa > hs:
        hs = sa
    if sa < ls:
        ls = sa
    ts += sa
    c  += 1
print('-'*50)
print("Total number of employees       : ", len(dc))
print("Total Salary paid to Employees  : ", ts)
print("Average Salary paid to Employees: ", ts/len(dc))
print("Highest Salary amount paid      : ", hs)
print("Lowest Salary amount paid       : ", ls)
    
    

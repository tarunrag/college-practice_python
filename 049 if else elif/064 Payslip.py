import sys

print("CALCULATE AND PRINT PAYSLIP\n")

print("Enter Employee Details....")
no =      input("Emp. No     : ")
nm =      input("Emp. Name   : ")
gr =      input("Grade(A/B/C): ")
if gr not in 'AaBbCc':
    print("\nInvalid Grade Entered !")
    #exit()
    sys.exit()
bp = eval(input("Basic Pay   : "))
print()

da = bp*0.4

if gr in 'Aa':
    hr = bp*0.15
    es = bp*0.15
    pf = da*0.085
elif gr in 'Bb':
    hr = bp*0.12
    es = bp*0.12
    pf = da*0.08
else:
    hr = bp*0.10
    es = bp*0.12
    pf = da*0.075
    
gs = bp + hr + da
dd = pf + es
np = gs - dd

print("Salary Pay Slip")
print("===============\n")

print("Empno     :", no, '\t\t\t', "Grade  :", gr)
print("Name      :", nm, '\n')

print("Basic Pay :", bp)
print("HRA       :", hr, '\t\t', "DA     :", da)
print("Gross     :", gs, '\n')	

print("PF        :", pf, '\t\t', "ESI    :", es)
print("Deductions:", dd, '\n')

print("Net Pay   :", str(np) + "/- Rs.")

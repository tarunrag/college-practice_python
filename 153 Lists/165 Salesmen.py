print("NESTED LIST - SALESMAN\n")

ls = []

while True:
    print("Enter Sales Personel's Details...\n")
    sl = input("Salesman No: ")
    na = input("Name       : ")
    ge = input("Gender     : ")
    se = input("Section    : ")

    print("Sales Amount in Four Quarters...\n")
    qt1 = eval(input("Qtr 1: "))
    qt2 = eval(input("Qtr 2: "))
    qt3 = eval(input("Qtr 3: "))
    qt4 = eval(input("Qtr 4: "))

    ls += [sl, na, ge, se, [qt1, qt2, qt3, qt4]],
    
    if input("Input More(y/n): ").lower() != 'y':
        break 
    print('\n')
    
##ls = [['1', 'Dawn', 'M', 'A', [1200, 2300, 4300, 5000]],
##      ['2', 'Tom', 'M', 'B', [2300, 4500, 1000, 5000]],
##      ['5', 'Sam', 'M', 'C', [1200, 2300, 3400, 5000]]]
   
print("SALES REPORT\n")

print("%-10s %-10s %-10s %-10s %12s %10s" %
    ("Slno", "Name", "Gender", "Section", "Total Sales", "Average"))

for no, na, ge, se, qt in ls:
    ts = sum(qt)
    av = ts/4
    print("%-10s %-10s %-10s %-10s %12d %10.2f" %
        (no, na, ge, se, ts, av))
          
      

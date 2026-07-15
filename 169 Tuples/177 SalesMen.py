tp = ()
n = 1
while True:
    print("LIST WITHIN TUPLE - SALESMAN\n")
 
    print("No.     :", n, '\n')

    print("Details of Salesman...")
    sn =     input("Salesman's No: ")
    na =     input("Name         : ")
    ge =     input("Gender       : ")
    se =     input("Section      : ")
    print()
    print("Sales Amount of 4 Quarters...\n")
    qt1 = eval(input("Qtr 1 : "))
    qt2 = eval(input("Qtr 2 : "))
    qt3 = eval(input("Qtr 3 : "))
    qt4 = eval(input("Qtr 4 : "))
 
    tp += (sn, na, ge, se, [qt1, qt2, qt3, qt4])
    n += 1 
     
    if input("Input More(y/n): ").lower() != 'y':
        break
    print('\n')

##tp = ('12', 'Thomas', 'M', 'E', [100, 200, 500, 600], 
##      '13', 'Mathew', 'M', 'E', [1002, 2340, 5644, 2300],
##      '24', 'George', 'M', 'A', [100, 5400, 2300, 900],
##      '36', 'Aarya',  'F', 'B', [1050, 2300, 900, 1200])
      

print("SALES REPORT\n")
print('%-10s %-10s %-10s %-15s %10s %15s' %
    ("Slno.", "Name", "Gender", "Section", "Total Sales", "Average"))
ts = mc = fc = 0
ht = lt = 0
for c in range(0, len(tp), 5):
    tt = sum(tp[c+4])
    av = tt/4
    print('%-10s %-10s %-10s %-15s %10s %15.2f' %
          (tp[c+0], tp[c+1], tp[c+2], tp[c+3], tt, av))

    if tp[c+2] in 'Mm':
          mc += 1
    if tp[c+2] in 'Ff':
        fc += 1
    ts += tt

    if c == 0:
        ht = lt = tt
        hn = ln = tp[c+1]
    if tt > ht:
        ht = tt
        hn = tp[c+1]
    if tt < lt:
        lt = tt
        ln = tp[c+1]
print()    
print("No. of Females:", fc)
print("No. of Males  :", mc)
print("Total Sales   :", ts)
print("Highest Total :", ht, '\t\t', "Name:", hn)
print("Lowest Total  :", lt, '\t\t', "Name:", ln)



    

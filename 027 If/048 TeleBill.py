print("CALCULATING & PRINTING TELEPHONE BILL\n")

print("Enter Subscribers Details.....")
nu =  int(input("enter Number: "))
nm =      input("enter Name: ")
lm = eval(input("Last Meter Reading    :"))
pm = eval(input("Present Meter Reading :"))
print()
FR = 180
TA = 12
FC = 100

tc = (pm-lm)
if tc < 100:
    cc = FC - tc
if tc > 100:
    cc = tc - FC


if tc <= 100:
    r = 0.00
    cr = 0
if tc > 100 and tc < 350:
    r = 1.00
    cr = tc-180
if tc > 350 and tc < 800:
    r = 1.20
    cr = 170 + 170*r
if tc > 800:
    r = 1.50
    cr = 170 + 450*1.2 + (800-tc)*r
tx = cr*TA/100
ta = tx + FC + cr

print("Number:", nu)
print("Name  :", nm)
print("Last Meter Reading   :", lm)
print("Present Meter Reading:", pm)
print("Telephone Bill\n\n")
print("Number       :", nu , '\t\t', "Name              :", nm, '\n')
print("L.M.R        :", lm , '\t\t', "Total Calls       :", tc)
print("P.M.R        :", pm , '\t\t', "Free Calls        :", FC)
print("\t\t\t\tCalls Charged      :", cc)
print("Call Charges :", cr)
print("Fixed Rent   :", FR,   '\t\t',  "Tax @",TA, "%   :",tx )
print("Total Amount :", ta, "/- Rs.") 



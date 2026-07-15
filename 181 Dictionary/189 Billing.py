print("BILLING\n")

dc = {}
c = 1
while True:
    print("Item", c)
    na =     input("Name: ")
    am = int(input("Amount: "))
    
    dc[na] = am
    c += 1
    if input("Input More(y/n): ").lower() != 'y':
        break

print("BILL DETAILS\n")

sn = 1
s  = 0
print("Slno.", "Item", "Amount", sep = '\t')
for na, am in dc.items():
    print(sn, na, am, sep = '\t')
    sn += 1
    s += int(am)
print('-'*25)
print("Total amount: ", s)

    

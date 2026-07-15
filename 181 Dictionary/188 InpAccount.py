print("INPUTING & PRINTING DICTIONARIES\n")

dc = {}
while True:
    ac = int(input("Account No.                  : "))
    na =     input("Name                         : ")
    ca =     input("Category(savings/current)    : ")
    ba = int(input("Balance                      : "))

    dc[ac] = [na, ca, ba]

    if input("Input more(y/n): ").lower() != 'y':
        break
    print('\n')
print()

print("Slno.", "acno.", "Name", "Catg.", "Balance", sep = '\t')
sn = 1
for ac, [na, ca, ba]  in dc.items():
    print(sn, ac, na, ca, ba, sep = '\t')
    sn += 1
    

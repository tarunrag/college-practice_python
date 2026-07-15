print("ITEM REPORT\n")
dc = {}
s = c = 0
while True:
    print("Item", c+1)
    na =      input("Name: ")
    pr = eval(input("Price: "))
    dc[na] = pr
    s += pr
    c += 1
    if input("Input more(y/n): ").lower() != 'y':
        break
    print('\n')
a = s/c
print()
print("Average Price: %0.2f\n" % a)
print("Item", "Price", "Remark", sep = '\t') 
for na, pr in dc.items():
    if pr < a:
        rm = "below"
    elif pr > a:
        rm = "above"
    else:
        rm = "equal"
    print(na, pr, rm, sep = '\t')
    


    
    

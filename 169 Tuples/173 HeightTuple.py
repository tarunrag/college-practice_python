print("HEIGHT TUPLE\n")

tp = (5.10, 5.5, 6.0, 5.9, 5.6, 5.3, 5.11)

print(tp, '\n')

av = sum(tp)/len(tp)

print("Average Height: %0.2f\n" % av)

print("Slno.", "Height", "Category", sep = '\t')
sn = 1
for v in tp:
    if v > av:
        rs = 'Above'
    elif v < av:
        rs = 'Below'
    else:
        rs = 'Equal'
    #print(sn, '%0.2f' % v, rs, sep = '\t')
    print(tp.index(v)+1, '%0.2f' % v, rs, sep = '\t') 
    sn += 1



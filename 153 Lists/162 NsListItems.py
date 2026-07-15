print("NESTED LIST - ITEMS\n")

ls = [['P1', 'Pencil HB2', 50, 20],
      ['P2', 'Ballpoint Pen', 30, 135],
      ['E1', 'Camel Eraser', 15, 40],
      ['B1', 'NoteBook', 60, 305],
      ['S1', 'Plastic Scale', 15, 20]]

print('Slno', 'ItCode', 'ItName\t', 'Price', 'Stk.Qty', sep = '\t')
sn = 1
for ic, nm, pr, sq in ls:
    print(sn, ic, nm, pr, sq, sep = '\t')
    sn += 1
    
print()
print('%-10s %-10s %-20s %10s %10s' %
      ('Slno', 'ItCode', 'ItName', 'Price', 'Stk.Qty'))
sn = 1
for ic, nm, pr, sq in ls:
    print('%-10s %-10s %-20s %10.2f %10d' % (sn, ic, nm, pr, sq))
    sn += 1
    

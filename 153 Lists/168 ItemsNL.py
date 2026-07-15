ls =  [[1, 'apple', 30, 50],
       [54, 'orange', 45, 65],
       [78, 'car toy', 20, 100],
       [100, 'spoon', 55, 15]]
mn = '''ITEM DETAILS

1.Append
2.Update
3.Delete
4.Search by...
    a) Slno
    b) ItCode
    c) ItName
    d) StockQty
    e) Price
5. List
6. Exit Program

Enter choice: '''

while True:
    ch = input(mn)
    if ch == '1':
        ic = int(input("Enter item code: "))
        na =     input("Enter item name: ")
        qt = int(input("Enter quantity : "))
        pr = int(input("Enter Price    : "))
        ls.extend([ic, na, qt, pr])
    elif ch == '2':
        pass
    elif ch == '3':
        pass
    elif ch == '4':
        pass
    elif ch == '5':
        print("%-10s %-10s %-10s %15s" %
            ("Item Code", "Item Name", "Quantity", "Price"))
        for ic, na, qt, pr in ls:
            print("%-10d %-10s %-10d %15s" %
                (ic, na, qt, pr))
    elif ch == '6':
        break
    else:
        print("Invalid Choice !")
    print('\n')

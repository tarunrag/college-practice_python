mn = '''
ITEMS – MENU DRIVEN

1. Append
2. Update
3. Delete
4. Search
5. View all items
6. Exit Program

Enter choice(1-6): '''

sm = '''
Search
   a. Item code
   b. Item name
   c. Price
   d. Stock qty

Enter choice(a-d): '''

while True:
    ch = input(mn)
    print()
    if ch == '1':
        print("Appending Data...\n")
        ic =      input("Item Code: ")
        na =      input("Item Name: ")
        pr = eval(input("Price    : "))
        sq =  int(input("Stock qty: "))

        if input("Append data?(y/n): ").lower() == 'y':
            dc[ic] = [na, pr, sq]
            print("Data Added !")
        else:
            print("Cancelled !")
    elif ch == '2':
        ik = input("Item Code to be updated: ")
        if ik in dc:
            na, pr, sq = dc[ik]
            print("Name: ", na)
            print("Price: ", pr)
            print("Stockqty:", sq)
    elif ch == '3':
        pass
    elif ch == '4':
        pass
    elif ch == '5':
        print("Item code", "Name", "Price", "Stock qty.", sep = '\t')
        for ic,  in dc.items():
            print(ic, na, pr, sq, sep = '\t')
    elif ch == '6':
        break
    print('\n')



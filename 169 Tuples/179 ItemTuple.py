tp = ('P1', 'Pencil', 10, 100,
      'E1', 'Eraser', 3, 25,
      'T1', 'Toy', 50, 20,
      'B1', 'Book', 25, 50,
      'S1', 'Scale', 30, 50)

mn = '''
ITEM DETAILS

1. Append
2. Search
3. Update
4. Delete
5. List
6. Exit Program

Enter Choice(1-6): '''

sm ='''
Search
   1. By Serial No. 
   2. By Itemcode
   Enter Choice: '''

while True:
    ch = input(mn)
    print()
    if ch == '1':
        ic =      input("Item Code: ")
        nm =      input("Item name: ")
        pr = eval(input("Price    :"))
        sq =  int(input("Stock Qty: "))
        print()
        if input("Append Details(y/n): ").lower() == 'y':
            tp += (ic, nm, pr, sq)
            print("Added !")
        else:
            print("Cancelled !")
            
    elif ch == '2':
        ch1 = input(sm)
        print()
        if ch1 == '1':
            sn = int(input("Enter serial number to be searched: "))
            if sn >= 1 and sn <= len(tp)//4:
                c = (sn-1)*4
                print("Item code:", tp[c+0])
                print("Item name:", tp[c+1])
                print("Price    :", tp[c+2])
                print("Stock Qty:", tp[c+3])
            else:
                print("Invalid Serial number !")
                
        elif ch1 == '2':
            cd = input("Enter item code to be searched: ")
            for c in range(0, len(tp), 4):
                if cd == tp[c+0]:
                    print("Item name:", tp[c+1])
                    print("Price    :", tp[c+2])
                    print("Stock Qty:", tp[c+3])
                    break
            else:
                print("Item code not found !")
        else:
            print("Invalid Choice !")
            
    elif ch == '3':
        sn = int(input("Enter serial number to be updated: "))
        if sn >= 1 and sn <= len(tp)//4:
            c = (sn-1)*4
            print("Item code:", tp[c+0])
            print("Item name:", tp[c+1])
            print("Price    :", tp[c+2])
            print("Stock Qty:", tp[c+3])
            if input("Update(y/n): ").lower() == 'y':
                ic =      input("Item Code: ")
                nm =      input("Item name: ")
                pr = eval(input("Price    : "))
                sq =  int(input("Stock Qty: "))
                print()
                if input("Confirm Update(y/n): ").lower() == 'y':
                    tp = tp[:c] + (ic, nm, pr, sq) + tp[c+4:]
                    print("Updated !")
                else:
                    print("Updation Cancelled !")
            else:
                print("Cancelled !")
        else:
            print("Invalid Serial number !")
            
            
    elif ch == '4':
        sn = input("Enter serial number to be deleted: ")
        if sn >= 1 and sn <= len(tp)//4:
            c = (sn-1)*4
            print("Item code:", tp[c+0])
            print("Item name:", tp[c+1])
            print("Price    :", tp[c+2])
            print("Stock Qty:", tp[c+3])
            if input("Delete(y/n): ").lower() == 'y':
                tp = tp[:c]+tp[c+4:]
                print("Deleted !")
            else:
                print("Cancelled !")
        else:
            print("Invalid Serial number !")
            
    elif ch == '5':
        print("Slno.", "ItCode", "Itname", "Price",  "StkQty", sep = '\t')
        sn = 1
        for c in range(0, len(tp), 4):
            print(sn, tp[c+0], tp[c+1], tp[c+2], tp[c+3], sep = '\t')
            sn += 1
            
    elif ch == '6':
        break
    else:
        print("Invalid Choice !")
    print('\n')
        

mn = '''
BOOKS - MENU DRIVEN

1. Append
2. Search by...
3. Update
4. Delete
5. List
6. Exit Program

Enter Choice(1-6): '''

sm = '''
Search by...
  1. Serial No.
  2. Bookcode
  3. Title
  4. Author
  5. Category
  Enter Choice(1-5): '''

##dc = {'12': ['harry potter', 'JK Rowling', 'Fiction', 265, 299],
##      '23': ['Love and War', 'Leo Tolstoy', 'Fiction', 600, 999],
##      '53': ['Hucklberry Finn', 'Mark Twain', 'Fiction', 300, 300],
##      '90': ['Cengage PYQ', 'H R Sharma', 'Education', 1000, 999],
##      '100':['JEE adv. PYQ', 'Ashish Arora', 'Education', 300, 600]}

dc = {}

while True:    
    ch = input(mn)
    print()
    if dc == {} and ch in '2345':
        print("No details Stored !\n")
        continue
    if ch == '1':
        print("Appending Data...\n")
        bc =     input("Book Code: ")
        ti =     input("Title    : ")
        au =     input("Author   : ")
        ca =     input("Category : ")
        pa = int(input("Pages    : "))
        pr = int(input("Price    : "))

        if input("Append data?(y/n): ").lower() == 'y':
            dc[bc] =  [ti, au, ca, pa, pr]
            print("Data Added !")
        else:
            print("Cancelled !")
           
    elif ch == '2':
        sb = input(sm)
        if sb == '1':
            sn = int(input("Serial number to be searched: "))
            c = 1
            fg = 0
            for bk, [ti, au, ca, pa, pr] in dc.items():
                if sn == c:
                    print("Book code:", bk)
                    print("Title    :", ti)
                    print("Author   :", au)
                    print("Category :", ca)
                    print("Pages    :", pa)
                    print("Price    :", pr)
                    fg = 1
                c += 1

            if fg == 0:
                print("Serial number Not found !") 
           
        elif sb == '2':
            bk = input("code to be searched: ")
            if bk in dc:
                ti, au, ca, pa, pr = dc[bk]
                print("Title   :", ti)
                print("Author  :", au)
                print("Category:", ca)
                print("Pages   :", pa)
                print("Price   :", pr)
            else:
                print("Not Found !")
        elif sb == '3':
            tt = input("Name of book to be searched: ")
            fg = 0
            for bk, [ti, au, ca, pa, pr] in dc.items():
                if tt == ti:
                    print("Book code:", bk)
                    print("Title    :", ti)
                    print("Author   :", au)
                    print("Category :", ca)
                    print("Pages    :", pa)
                    print("Price    :", pr)
                    fg = 1
            if fg == 0:
                print("Title not found !")

        elif sb == '4':
            na = input("Name of Author to be searched: ")
            fg = 0
            for bk, [ti, au, ca, pa, pr] in dc.items():
                if na == au:
                    print("Book code:", bk)
                    print("Title    :", ti)
                    print("Author   :", au)
                    print("Category :", ca)
                    print("Pages    :", pa)
                    print("Price    :", pr)
                    fg = 1
            if fg == 0:
                print("Author not found !")
          
        elif sb == '5':
            ct = input("Category to be searched: ")
            fg = 0 
            for bk, [ti, au, ca, pa, pr]  in dc.items():
                if ct == ca:
                    if fg == 0:
                        print("Book code", "Title", "Author", "Category", "Pages", "Price", sep = '\t')
                    print(bc, ti, au, ca, pa, pr, sep = '\t')
                    fg = 1
            if fg == 0:
                print("Category Not Found !")
            
    elif ch == '3':
        bk = input("Book code to be updated: ")
        if bk in dc:
            ti, au, ca, pa, pr = dc[bk]
            print("Title    :", ti)
            print("Author   :", au)
            print("Category :", ca)
            print("Pages    :", pa)
            print("Price    :", pr)
            
            if input("Update(y/n): ").lower() == 'y':
                ti =     input("Title    : ")
                au =     input("Author   : ")
                ca =     input("Category : ")
                pa = int(input("Pages    : "))
                pr = int(input("Price    : "))

                if input("Confirm update(y/n): ").lower() == 'y':
                    dc[bk] = ti, au, ca, pa, pr
                    print("Updated !")
                else:
                    print("Updation Cancelled !")
            else:
                print("Cancelled !")
        else:
            print("Invalid Book code !")
            
                
        
    elif ch == '4':
        bk = input("Book code to be deleted: ")
        if bk in dc:
            ti, au, ca, pa, pr = dc[bk]
            print("Title    :", ti)
            print("Author   :", au)
            print("Category :", ca)
            print("Pages    :", pa)
            print("Price    :", pr)
            
            if input("Delete(y/n): ").lower() == 'y':
                del dc[bk]
                print("Deleted !")
            else:
                print("Cancelled !")
        else:
            print("Invalid Book Code !")
                         
    elif ch == '5':
        print("Book code", "Title", "Author", "Category", "Pages", "Price", sep = '\t')
        for bc, [ti, au, ca, pa, pr] in dc.items():
            print(bc, ti, au, ca, pa, pr, sep = '\t')
    elif ch == '6':
        break
    print('\n')


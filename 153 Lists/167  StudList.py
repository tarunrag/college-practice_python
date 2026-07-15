mn = '''
STUDENT DETAILS

1. Append
2. Update
3. Delete
4. Search
   a. Rollno
   b. Name
   c. Class
   d. Percentage
5. View List
6. Exit Program

Enter Choice(1-6): '''

sm = '''
Search
   a. Rollno
   b. Name
   c. Class
   d. Percentage

   Enter choice(a-d): '''

ls = [[10, 'Arjun', 12, 'A', 94],
      [11, 'Shreya', 12 , 'A', 93],
      [12, 'Meghna', 12, 'A', 90],
      [13, 'Niya', 11, 'B', 91],
      [14, 'Arjun', 11, 'B', 88],
      [15, 'Bibi', 11, 'B', 93]]
      
while True:
    ch = input(mn)
    print()

    if ch == '1':
        print("Add Details...")
        rn =  int(input("Roll no   : "))
        na =      input("Name      : ")
        cl =  int(input("Class     : "))
        dv =      input("Division  : ")
        pr = eval(input("Percentage: "))
        print()
        if input("Add Details(y/n): ").lower() == 'y':
            ls.extend([rn, na, cl, dv, pr])
            print("Details Added !")
        else:
            print("Cancelled !")

    elif ch == '2':
        ro = int(input("Roll number to update: "))
        c = 0
        for rn, na, cl, dv, pr in ls:
            if rn == ro:
                print("Name      :", na)
                print("Class     :", cl)
                print("Division  :", dv)
                print("Percentage:", pr, '\n')
                if input("Update(y/n): ").lower() == 'y':
                    print('Update info...')
                    rn =  int(input('Roll no   : '))
                    na =      input("Name      : ")
                    cl =  int(input("Class     : "))
                    dv =      input("Division  : ")
                    pr = eval(input("Percentage: "))
                    print()
                    if input('Confirm Update(y/n):').lower() == 'y':
                        ls[c] = rn, na, cl, dv, pr
                        print("Updated !")
                    else:
                        print("Updation Cancelled !")
                else:
                    print("Cancelled !")
                break
            c += 1
        else:
            print("Given Roll no NOT found !")
            
 
    elif ch == '3':
        ro = int(input("Roll number to delete: "))
        c = 0
        for rn, na, cl, dv, pr in ls:
            if rn == ro:
                print("Name      :", na)
                print("Class     :", cl)
                print("Division  :", dv)
                print("Percentage:", pr, '\n')
                if input("Delete(y/n): ").lower() == 'y':
                    ls.pop(c)
                    print("Deleted !")
                else:
                    print("Cancelled !")
                break
            c += 1
        else:
            print("Given Roll no NOT found !")
            
    elif ch == '4':
        ch1 = input(sm).lower()
        print()

        if ch1 == 'a':
            ro = int(input("Roll No: "))
            print()
            for rn, na, cl, dv, pr in ls:
                if ro == rn:
                    print("Name      :", na)
                    print("Class     :", cl)
                    print("Division  :", dv)
                    print("Percentage:", pr, '\n')
                    break
            else:
                print("Given Roll No NOT found!")
        elif ch1 == 'b':
            nm = input("Name: ")
            print()
            sn = 1
            for rn, na, cl, dv, pr in ls:
                if nm.lower() == na.lower():
                    if sn == 1:
                        print("%-10s %-10s %-20s %-10s %-10s %10s" %
                              ("Slno", "Roll no", "Name", "Class", "Division", "Percentage"))

                    print("%-10s %-10s %-20s %-10s %-10s %10.2f" %
                          (sn, rn, na, cl, dv, pr))
                    sn += 1
            if sn == 1:
                print("Given Name NOT found!")

        elif ch1 == 'c':
            cs = input("Class: ")
            print()
            sn = 1
            for rn, na, cl, dv, pr in ls:
                if cs.lower() == cl.lower():
                    if sn == 1:
                        print("%-10s %-10s %-20s %-10s %-10s %10s" %
                              ("Slno", "Roll no", "Name", "Class", "Division", "Percentage"))

                    print("%-10s %-10s %-20s %-10s %-10s %10.2f" %
                          (sn, rn, na, cl, dv, pr))
                    sn += 1
            if sn == 1:
                print("Given Class NOT found!")
        elif ch1 == 'd':
            pass
        else:
            print("Invalid choice !")

    
    elif ch == '5':
        print("%-10s %-10s %-20s %-10s %-10s %10s" %
              ("Slno", "Roll no", "Name", "Class", "Division", "Percentage"))
        sn = 1
        for rn, na, cl, dv, pr in ls:
            print("%-10s %-10s %-20s %-10s %-10s %10.2f" %
                  (sn, rn, na, cl, dv, pr))
            sn += 1
              
    elif ch == '6':
        break
    else:
        print("Invalid choice !")
    print('\n')










    
              
        

    

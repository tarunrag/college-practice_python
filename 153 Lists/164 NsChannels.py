print("NESTED LIST - CHANNELS\n")

##n = int(input("Enter No. Channel details to input: "))
##print()
##ls = []
##for c in range(1, n+1):
##    print("Number", c)
##    cno =      input("Channel no  : ")
##    cna =      input("Channel Name: ")
##    rat = eval(input("Rating      : "))
##
##    ls += [cno, cna, rat],
##    print()

ls = [['114', 'Mathrubhumi', 3],
      ['125', 'Manorama', 3],
      ['145', 'Asianet', 5]]

print("CHANNEL REPORT\n")

print("%-10s %-10s %-20s %10s" %
    ("Slno.", "Ch.no", "Ch.Name", "Rating"))
sno = 1
for cno , cna , rat in ls:
    print("%-10s %-10s %-20s %10.2f" %
        (sno, cno, cna, rat))
    if sno == 1:
        hr = lr = rat
        hn = ln = cna
    if rat > hr:
        hr = rat
        hn = cna
    if rat < lr:
        lr = rat
        ln = cna
    sno += 1
print()
print("Highest Rated Channel:", hn)
print("Lowest Rated Channel :", ln)


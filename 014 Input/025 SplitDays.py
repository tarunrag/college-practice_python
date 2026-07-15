print("SPLIT DAYS\n")

ds = int(input("Enter Days: "))
print()

yr = ds//365
mn = (ds%365)//30
dd = (ds%365)%30

print(ds, "Days Contain....")
print(yr, "Year(s),")
print(mn, "Month(s) &")
print(dd, "Day(s)")

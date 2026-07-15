print("SPLIT SECONDS\n")

se = int(input("Enter Seconds: "))
print()

hr = se//3600
mn = (se%3600)//60
ss = (se%3600)%60

print(se, "seconds contains....")
print(hr, "Hour(s),")
print(mn, "Min(s) &")
print(ss, "Second(s)")




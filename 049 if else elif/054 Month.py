print("MONTH IN WORDS\n")

m = int(input("Enter Month (1-12): "))
print()

if m == 1:
   ms = "January"
elif m == 2:
   ms = "February"
elif m == 3:
   ms = "March"
elif m == 4:
   ms = "April"
elif m == 5:
   ms = "May"
elif m == 6:
   ms = "June"
elif m == 7:
   ms = "July"
elif m == 8:
   ms = "August"
elif m == 9:
   ms = "September"
elif m == 10:
   ms = "October"
elif m == 11:
   ms = "November"
elif m == 12:
   ms = "December"
else:
   ms = "Invalid Month Value"
   
print("Month", m, "represents.....", ms, "!")

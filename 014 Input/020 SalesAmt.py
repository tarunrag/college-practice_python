print("CALCULATE SALES AMOUNT\n")

qt =  int(input("Quantity  : "))
rt = eval(input("Rate      : "))
ta = eval(input("Tax amount: "))
print()

sa = qt*(rt+ta)

print('Sales Amount = Rs.' + str(round(sa, 2)) + '/-')

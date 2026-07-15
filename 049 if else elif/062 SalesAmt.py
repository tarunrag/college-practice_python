print("SALES AMOUNT CALCULATION\n")

ic =  int(input("Item Code: "))
nm =      input("Item Name: ")		
pr = eval(input("Price    : "))
qt =  int(input("Quantity : "))
print()

sa = pr*qt
if sa <= 1000:
    dp = 0
elif  sa <= 5000:
    dp = 2
elif  sa <= 10000:
    dp = 5
else:
    dp = 10

da = sa*dp/100
ap = sa - da

print("Sales Amount   :", sa)
print("Discount %     :", dp, "%")
print("Discount Amount:", da)
print("Amount Payable :", ap)

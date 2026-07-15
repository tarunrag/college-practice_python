print("SALES AMOUNT CALCULATION\n")

ic =  int(input("Item Code: "))
nm =      input("Item Name: ")		
pr = eval(input("Price    : "))
qt =  int(input("Quantity : "))
print()
        
sa = pr*qt
if sa <= 1000:
    dp = 0
if sa > 1000 and sa <= 5000:
    dp = 2
if sa > 5000 and sa <= 10000:
    dp = 5
if sa >10000:
    dp = 10

da = sa*dp/100
ap = sa - da

print("Sales Amount   :", sa)
print("Discount %     :", dp, "%")
print("Discount Amount:", da)
print("Amount Payable :", ap)


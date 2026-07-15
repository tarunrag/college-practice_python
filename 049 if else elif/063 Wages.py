print("WAGE CALCULATION\n")

en =     input("Emp. Number : ")
nm =     input("Emp. Name   : ")
hw = int(input("Hours Worked: "))
print()

if hw <= 40:
    wg = hw*100
elif hw <= 60:
    wg = (40*100) + (hw-40)*150
else:
    wg = (40*100) + (20*150) + (hw-60)*200

print("Wages:", wg)

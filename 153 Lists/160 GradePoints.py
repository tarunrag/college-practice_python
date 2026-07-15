print("GRADE POINT LIST\n")

ls = list(eval(input("Enter Grade points: ")))
print()

av = sum(ls)/len(ls)
print("Average Grade Point is: %0.2f\n" % av)

print("Below or Equal to Average\n")
for v in ls:
    if v <= av:
        print('%0.2f' % v,  end = ' ')
print('\n')

print("Above Average\n")
for v in ls:
    if v > av:
        print('%0.2f' % v,  end = ' ')
print('\n')

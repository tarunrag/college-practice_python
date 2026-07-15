print("LIST ELEMENT WISE WITH SUM, AVERAGE, LARGEST AND SMALLEST VALUES\n")

lst = [13, 40, 22, 11, 25]

print("Full List Element wise...\n")
c = s = 0
for v in lst:
    print(v, end = ' ')
    s += v
    if c == 0:
        lg = sm = v
    if v > lg:
        lg = v
    if v < sm:
        sm = v
    c += 1
a = s/c

print('\n')
print("Sum    :", s)
print("Average:", a, '\n')

print("Largest Value : ", lg)
print("Smallest Value: ", sm, '\n')


print("Sum    :", sum(lst))
print("Average:", sum(lst)/len(lst), '\n')

print("Largest Value : ", max(lst))
print("Smallest Value: ", min(lst), '\n')






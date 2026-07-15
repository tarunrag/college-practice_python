print("TUPLE ELEMENT WISE WITH SUM, AVERAGE, LARGEST AND SMALLEST VALUES\n")

tp = (13, 40, 22, 11, 25)

print("Tuple Element wise...")
s = c = 0
for v in tp:
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

print("Sum    :", sum(tp))
print("Average:", sum(tp)/len(tp), '\n')

print("Largest Value :", max(tp))
print("Smallest Value: ", min(tp), '\n')

print("Sum    :", s)
print("Average:", a, '\n')


print("Largest Value :", lg)
print("Smallest value:", sm)




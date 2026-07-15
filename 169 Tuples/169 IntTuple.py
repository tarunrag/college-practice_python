print("INTEGER TUPLE\n")

tp = (13, 40, 22, 11, 25)

print("Tuple:", tp, '\n')

print("Fourth Element:", tp[3], '\n')

print("Tuple Element wise...")
for v in tp:
    print(v, end = ' ')
print('\n')

print("Tuple Index wise...")
for c in range(len(tp)):
    print(str(c)+':', tp[c], end = '\t')

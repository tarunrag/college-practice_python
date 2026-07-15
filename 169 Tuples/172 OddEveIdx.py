print("ODD AND EVEN VALUES IN TUPLE WITH INDEX\n")

tp = (10, 15, 24, 32, 17, 5 )

print("Full Tuple...")
for v in tp:
    print(v, end = '\t')
print('\n')

print("Even Index Tuple Elements...")
for c in range(len(tp)):
    if c%2 == 0:
        print(str(c)+':'+ str(tp[c]), end = '\t')
print('\n')

print("Odd Index Tuple Elements...")
for c in range(len(tp)):
    if c%2 != 0:
        print(str(c)+':'+ str(tp[c]), end = '\t')



print("SUM, AVERAGE, LARGEST AND SMALLEST VALUES IN THE TUPLE\n")

n = int(input("Number of values to input: "))
tp = ()
for c in range(n):
    v = int(input("Enter value "+str(c+1)+': '))
    tp = tp + (v, )

print("Tuple  : ", tp, '\n')

print("Sum    :", sum(tp))
print("Average:", sum(tp)/len(tp), '\n')

print("Largest Value:", max(tp))
print("Smallest Value:", min(tp))
    
    
    

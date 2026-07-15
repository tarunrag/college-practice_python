print("INTEGER LIST\n")

lst = [13, 40, 22, 11, 25]

print("Full List:", lst, '\n')

print("Second Element:", lst[1], '\n')

print("Full List Element wise...\n")
for v in lst:
    print(v, end = ' ')
print('\n')
    
print("Full List Index wise...\n")  
for c in range(0, len(lst)):
    print(lst[c], end = ' ')
print('\n')

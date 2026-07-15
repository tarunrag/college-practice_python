print("ODD AND EVEN VALUES IN TUPLE\n")

tp = (12, 24, 3, 10, 7, 21)

print("Tuple...")
for v in tp:
    print(v, end = ' ')
print('\n')

print("Even Elements in Tuple with their index in ()...")
for c in range(len(tp)):
    if tp[c]%2 == 0:
        #print(str(tp[c])+'('+str(c)+')', end = '\t')
        print('%d(%d)' % (tp[c], c), end = '\t')
print('\n')
    
print("Odd Elements in Tuple with their index in ()...")
for c in range(len(tp)):
    if tp[c]%2 != 0:  
        #print(str(tp[c])+'('+str(c)+')', end = '\t')
        print('%d(%d)' %(tp[c], c), end = '\t')
print('\n')
   
    
        


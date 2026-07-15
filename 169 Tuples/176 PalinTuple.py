print("INPUT N VALUES TO A TUPLE AND CREATING A PALINDROME TUPLE \n")

print("Enter values...\n")
tp = ()
c = 1
while True:
    va = eval(input("Value "+str(c)+': '))
    tp += (va, )
    c += 1
    
    if input("Input more(y/n): ").lower() != 'y':
        break
    print('\n')
print()

print("Full List...")
for v in tp:
    print(v, end = '\t')
print('\n')

print("Palindrome Elements in List...")
for v in tp:
    if str(v)[::-1] == str(v):
        print(v, end = '\t')
    
    
    

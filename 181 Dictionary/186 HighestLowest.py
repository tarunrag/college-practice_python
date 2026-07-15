print("INPUTING & PRINTING DICTIONARIES\n")
dc = {}
while True:
    
    na =      input("Name      : ")
    pr = eval(input("Percentage: "))
    print('\n')

    dc[pr] = na

    if input("Input More(y/n): ").lower() != 'y':
        break
    print('\n')


print("Highest Scorer's Details...\n")
print("Name", '\t', "Percentage")
for k in dc: 
    if k ==  max(dc):
        print(dc[k], '\t', k)
print('\n')

print("Lowest Scorer's Details...\n")
print("Name", '\t', "Percentage")
for k in dc:
    if k == min(dc):
        print(dc[k], '\t', k)

            
        
            

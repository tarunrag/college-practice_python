print("NAME AND PERCENTAGE\n")
ls = [1, 'Sam', 80, 31, 'Ben', 90, 40, 'Raju', 85, 62, 'Babu', 75]

print("Rollno", "Name", "Percentage", sep = '\t')

s = 0 
for c in range(0, len(ls), 3):
    print(ls[c+0], ls[c+1], ls[c+2], sep = '\t')
    s += ls[c+2]

a = s/(len(ls)//3)

print("Average %%: %0.2f\n" % a)

print("Below or Equal to Average")
for c in range(0, len(ls), 3):    
    if ls[c+2] <= a:
        print(ls[c+0], ls[c+1], ls[c+2], sep = '\t')
print()

print("Above Average")
for c in range(0, len(ls), 3):
    if ls[c+2] > a:
        print(ls[c+0],  ls[c+1], ls[c+2], sep = '\t')
        
        

    
    

    


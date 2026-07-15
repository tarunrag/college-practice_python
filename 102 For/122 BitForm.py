print("BIT FORM PATTERN\n")

n = int(input("Enter no. of lines to print: "))
print()

for r in range(1, n+1):
    for c in range(1, r+1):
        print((r+c+1)%2, end = ' ')
    print()
        
print()
for r in range(n+1):
    for c in range(1, r+1):
        print((r+c+1)%2, end = ' ')
    print()
        
        

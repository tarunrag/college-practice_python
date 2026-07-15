print("SPECIAL PATTERN 2\n")

n = int(input("Enter no: lines to print: "))
print()

for r in range(1, n+1):
    for c in range(1, n-r+1):
        print(end = ' ')
    for c in range(1, r+1):
        if r == 1 or r == n or c == 1 or c == r:
            print('&', end = ' ')
        else:
            print(end = '  ')
    print()
        

print("STAR PATTERN - 1\n")

n = int(input("Number of lines to print: "))
print()

for r in range(1, n+1):
    for c in range(1, r+1):
        print('*', end = ' ')
    print()

for r in range(n):
    for c in range(r+1):
        print('*', end = ' ')
    print()
    

for r in range(1, n+1):
    print('* '*r)


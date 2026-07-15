import sys

print("FLOYD'S TRIANGLE\n")

n = int(input("Enter Last value: "))
print()

v = 1
for r in range(1, n+1):
    for c in range(1, r+1):
        print(v, end = ' ')
        if v == n:
            sys.exit()
        v += 1
    print()
    

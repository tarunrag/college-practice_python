print("ODD AND EVEN VALUES IN LIST")

ls = list(eval(input("Enter values for list: ")))
print()

print("Full List...")
for v in ls:
    print(v, end = ' ')
print('\n')

print("Even Elements in List...")
for v in ls:
    if v%2 == 0:
        print(v, end = ' ')
print('\n')

print("Odd Elements in List...")
for v in ls:
    if v%2 != 0:
        print(v, end = ' ')

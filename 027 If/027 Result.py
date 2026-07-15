print("FIND RESULT\n")

m = float(input("Enter Marks scored: "))
print()

if m < 33.5:
    print("Result: Failed")
if m >= 33.5:
    print("Result: Passed")

print('Result:', end=' ')
if m < 33.5:
    print("Failed")
if m >= 33.5:
    print("Passed")

if m < 33.5:
    rs = "Failed"
if m >= 33.5:
    rs = "Passed"
print("Result:", rs)

    

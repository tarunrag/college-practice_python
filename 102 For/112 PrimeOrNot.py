while True:
print("INPUT AN INTEGER AND PRIME OR NOT\n")

v = int(input("Enter value: "))
print()

v = abs(v)
if v == 0 or v == 1:
    print("Neither prime nor composite")
else:
    for c in range(2, v):
        if v%c == 0:
            print("Not a prime number !")
            break
    else:
        print("Prime number !")

    ch = input("Continue?(Y/N): ")
    print()
    
    if ch != 'Y' and ch != 'y':
        break
    print('\n')

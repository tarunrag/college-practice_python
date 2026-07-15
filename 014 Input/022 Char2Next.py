print("ASCII, NEXT & PREVIOUS CHARACTER\n")

ch = input("Enter a character: ")
print()

ac = ord(ch)

print("ASCII Value        =", ac)
print("Previous Character =", chr(ac-1))
print("Next Character     =", chr(ac+1))


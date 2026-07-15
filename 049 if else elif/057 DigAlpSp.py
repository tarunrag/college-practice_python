print("DIGIT, ALPHABET OR SPECIAL CHARARCTER\n")

ch = input("enter character: ")
print()

if ch >= "0" and ch <= "9":
    print("A Digit !")
elif ch >= "A" and ch <= "Z":
    print(" An Upper case Alphabet !")
elif ch >= "a" and ch <= "z":
    print("A Lower case Alphabet !")
else: 
    print("A Special character !")
    

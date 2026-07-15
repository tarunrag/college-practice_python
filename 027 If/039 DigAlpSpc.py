print("DIGIT, ALPHABET OR SPECIAL CHARARCTER\n")

ch = input("Enter a  character: ")
print()

if ch >= "0" and ch <= "9":
    print("A Digit !")

if ch >= "A" and ch <= "Z":
    print(" An Upper case Alphabet !")
if ch >= "a" and ch <= "z":
    print("A Lower case Alphabet !")

if not (ch >= '0' and ch <= '9' or
        ch >= 'A' and ch <= 'Z' or
        ch >= 'a' and ch <= 'z'):
    print("A Special character !")
    
    

    
            

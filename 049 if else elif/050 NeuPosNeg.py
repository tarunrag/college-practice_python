print("NEUTRAL, POSITVE OR NEGATIVE VALUE\n")

v = eval(input("Enter a value: "))
print()

if v == 0:
    ms =  "Neutral"
elif v > 0:
    ms = "Positive"
else:
    ms = "Negative"
    
print("Value", v, "is", ms, "!")

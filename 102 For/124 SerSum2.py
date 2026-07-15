print("Series - 1 + x + x^2 + x^3 till x^n\n")

n = int(input('Enter power until which to show: '))
x = int(input('Enter an integer: '))
print()
s = 0

for p in range(n+1):
    s += x**p
print('Series: ', s)

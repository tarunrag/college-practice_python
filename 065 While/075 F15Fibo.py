print("FIBONACCI VALUES ( FIRST 15 VALUES)\n")

a = -1
b =  1
c =  0 
n = 1
while n <= 15:
    print(c)
    a = b
    b = c
    c = a + b
    n = n + 1
print()


a, b, n = -1, 1, 1
while n <= 15:
    print(a+b)
    a, b, n = b, a+b, n+1
    
    


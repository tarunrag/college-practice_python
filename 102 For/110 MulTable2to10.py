print("TABLES FROM 2 TO 10 (EACH 20 TIMES)\n")

for v in range(2,11):
    for n in range(1,21):
        print(v, '*', n, '=', v*n)
    if v < 10:
        input('Press ENTER to Continue...')
        print()
        
        

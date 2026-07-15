print("DAYS IN MONTH\n")

while True:
    y = int(input("Year : "))
    m =     input("Month: ")

    ds = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October':31, 'November':30, 'December':31}
    dy = {'January': 31, 'February': 29, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October':31, 'November':30, 'December':31}
    if y%4 == 0 and y%100 != 0:
        for k in dy:
            if m == k:
                print('Days:', dy[k])
                
    else:
        for k in ds:
            if m == k:
                print('Days:', ds[k])

    if input("Check again(y/n): ").lower() != 'y':
        break
    print('\n')
    
        

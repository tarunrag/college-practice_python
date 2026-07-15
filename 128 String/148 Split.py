while True:
    
    print("SPLITTING\n")

    dt = input("Enter date(d/m/y): ")
    print()

    d, m, y = dt.split('/')

    print("Day  :", d)
    print("Month:", m)
    print("Year :", y, '\n')

    if input("Check again(Y/N): ").lower() != 'y':
        break
    print('\n')
    

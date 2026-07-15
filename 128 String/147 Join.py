while True:
    print("JOIN\n")

    d = input("Enter Day(1-31)  : ")
    m = input("Enter Month(1-12): ")
    y = input("Enter Year       : ")
    print()

    dt = '/'.join([d, m, y])

    print("Date entered         :", dt, '\n')


    if input("Check another(Y/N): ").lower() != 'y':
        break
    print('\n')
    

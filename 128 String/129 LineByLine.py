print('WORDS LINE BY LINE\n')

st = input('Enter a string: ')
print()

for ch in st:
    print(ch, end = '')
    if ch == ' ':
        print()
print('\n')
for ch in st:
    if ch != ' ':
        print(ch, end = '')
    else:
        print()
    

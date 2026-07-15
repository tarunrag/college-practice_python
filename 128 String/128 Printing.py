print('PRINTING STRING\n')

st = input('String: ')
print()

print('Character Wise...')
for ch in st:
    print(ch, end = ' ')
print('\n')

print('Character Wise...Using Index')
for c in range(len(st)):
    print(st[c], end = ' ')
print('\n')

print('Character Wise...Using Negative Index')
for c in range(-len(st), 0):
    print(st[c], end = ' ')
print('\n')

print('In Reverse...')
for c in range(len(st)-1, -1, -1):
    print(st[c], end = ' ')
print('\n')

print('In Reverse...Using Negative index')
for c in range(-1, -len(st)-1, -1):
    print(st[c], end = ' ')
print('\n')


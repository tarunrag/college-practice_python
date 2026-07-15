print("PRINTING DICTIONARIES\n")

ds = {1: 98.5, 2: 66, 3: 89.5}

print("Rollno & Percentage")
print(ds, '\n')

print("Keys...")
print(ds.keys(), '\n')

print("Values...")
print(ds.values(), '\n')

print("Items:")
print(ds.items())

for k in ds:
    print(k, '\t', ds[k])

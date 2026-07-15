print("AVERAGE WEIGHT\n")

ds = {'Rajesh': 58.5, 'Mini': 52.0, 'Jayan': 56.0, 'John': 57.5}

print("Name & Weight")
print(ds)

s = c = 0
for k in ds:
    s += ds[k]
    c += 1
    av = s/c

print("Average Weight:", av, '\n')

print("Name", '\t', "Weight", "Remark")
for k in ds:
    if ds[k] < 50:
        re = "Normal !"
    elif ds[k] > 55:
       re = "Obese !"
    print(k, '\t', ds[k], re)
    
        

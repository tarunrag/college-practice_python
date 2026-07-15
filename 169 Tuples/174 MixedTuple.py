print("CLASS RESULTS\n")

tp = (1, 'Sam', 80, 90, 75, 60, 52,
      31, 'Ben', 90, 49, 62, 70, 60, 
      40, 'Raju', 85, 54, 25, 75, 85,
      62, 'Babu', 75, 64, 72, 80, 56)

print("Rollno.", "Name", "m1", "m2", "m3", "m4", "m5", "Result", sep = '\t')
for c in range(0, len(tp), 7):
    #if tp[c+2] < 35 or tp[c+3] < 35 or tp[c+4] < 35 or tp[c+5] < 35  or  tp[c+6] < 35:
    if min(tp[c+2: c+7]) < 35:
        rs = 'Failed'
    else:
        rs = 'Passed'
    print(tp[c+0], tp[c+1], tp[c+2], tp[c+3], tp[c+4], tp[c+5], tp[c+6], rs, sep = '\t')
    
    


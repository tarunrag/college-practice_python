print("NESTED LIST - STUDENT\n")

ls = [[31, 'SAM', 12, 'A', [80, 70, 95, 85, 75]],
      [44, 'TARUN', 12, 'C', [99, 95, 92, 98, 94]],
      [45, 'THOMAS', 12, 'C', [95, 96, 33, 90, 85]]]

for rl, na, cl, dv, mk in ls:
    print('Roll No:', rl, '\t\t', 'Name    :', na)
    print('Class  :', cl, '\t\t', 'Division:', dv, '\n')

    print("Marks Scored..")
    print("Eng", "Mat", "Phy", "Chm", "C.S", sep = '\t')
    print(mk[0], mk[1], mk[2], mk[3], mk[4], sep = '\t')
    print()
    #tt = mk[0] + mk[1] + mk[2] + mk[3] + mk[4]
    tt = sum(mk)
    pr =  tt/5
    #if mk[0] < 35 or mk[1] < 35 or mk[2] < 35 or mk[3] < 35 or mk[4] < 35:
    if min(mk) < 35:
        rs = 'Failed'
    else:
        rs = 'Passed'
    print("Total Marks:", tt)
    print("Percentage :", pr)
    print("Result     :", rs)
    print('='*80)
    print()

    

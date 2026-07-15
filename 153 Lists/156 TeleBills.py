ls = [123456, 'skibidi', 2000, 3000
      234567, 'hello', 3000, 4000
      

no = input("Number: ")
lm = int(input("Last Meter Reading   :"))
pm = int(input("Present Meter Reading:"))
print()

FC = 100
FR = 180
TP = 12

for c in range(0, len(ls), 4):
    no = ls[c+0]
    nm = ls[c+1]
    lm = ls[c+2]
    pm = ls[c+3]

    tc = pm-lm
    cc = 0
    if tc > FC:
        cc = tc-FC

    if tc >= FC:
        ch = 0
    if tc > FC and tc <= 350:
        ch = (tc-FC)*1.0
    if tc > 350 and tc <= 800:
        ch = (350 - FC)*1.0 + (tc-350)*1.2
    if tc > 800:
      ch = (350-FC)*1.0 + (450*1.2) + (tc-800)*1.5
      tx = ch*TP/100
      ta = ch + FR + tx
      
        



import re
i=0

file = open("aodv10.tr",'r')
data = file.readlines()[10:]
for line in data:
   sline = line.split(" ")
   try:
     for i in range (0,9):
        if sline[0] == 's' or sline[1]=='s':
                if sline[19]=='MAC' or sline[20]=='MAC':
                    sent[i] = sent[i] + int(sline[8])
   except:
     continue

for i in range(0,10):
    print"Value in", i, "is :", sent[i]



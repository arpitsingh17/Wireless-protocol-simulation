import re
from sys import argv

i=0
delay=0
sent=0
recv=0
time0=0
tim1=0
t1=0
sentdict = dict()
recvdict = dict()
delaylist = []


file = open(argv[1],'r')
data = file.readlines()

for line in data:
   sline = line.split(" ")
   try:
        if sline[0] == 's' or sline[1]=='s' :
          if sline[3]=='AGT' or sline[4]=='AGT':
              if sline[7]=='cbr' or sline[8]=='cbr':
                  sent +=1
              else:
                  continue


        elif sline[0] == 'r' or sline[1]=='r':
            if sline[3]=='AGT' or sline[4]=='AGT':
                if sline[7] == 'cbr' or sline[8] == 'cbr':
                    recv +=1
                else:
                    continue

   except:
     continue

#pecentage of packet deliverd
perdelievered = float(recv)/float(sent)*100

#delay
for line in data:
   sline = line.split(" ")
   if sline[3] == 'AGT':
        if sline[7] == 'cbr' or sline[8] == 'cbr':

            if sline[0]=='s':
                #seq=sline[6]
                if sline[6] not in sentdict.keys():
                    sentdict[sline[6]]= sline[1]

            elif sline[0]=='r':
                if sline[6] not in recvdict.keys():
                    recvdict[sline[6]]= sline[1]

for item in sentdict.keys():
    if item in recvdict.keys():
        delaylist.append(float(recvdict[item]) - float(sentdict[item]))
i =0
delay1 = 0
for delay in delaylist:
    delay1 += delay

    i+=1








print "Number of packets sent:- ",sent
print "Number of packets received:- ", recv
print "Percentage of packet delivered:- ", perdelievered

#print delaylist
print "Average delay:- ",delay1/i

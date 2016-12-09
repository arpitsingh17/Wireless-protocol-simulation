#Arpit Singh 010810514
#Ankita Chandrachud 010804833
#Program to extract data and calculate the throughput

import re

file = open("S11.tr.tr",'r')
data = file.readlines()[2:]
sent0=0
sent1= 0
r0=0
r1=0
dropped=0
throughput0 = 0
throughput1 = 0
time1=[]
sent00=0
sent11=0
r00=0
r11=0
time0=0
timen=0
time2=[]



for line in data:
   sline = line.split(" ")

   try:

           #print(sline[7])
           if sline[0] == 's':
               if sline[2] == '_0_' :
                   sent0 = sent0 + int(sline[8])
                   try:
                       if sline[7]=='tcp':
                         sent00=sent00+int(sline[8])
                         time1.append(sline[1])
                   except:
                         continue

               else:
                   sent1 = sent1 + int(sline[8])
                   try:
                       if sline[7]=='tcp':
                         sent11=sent11+int(sline[8])

                   except:
                       continue

           elif sline[0] == 'r':
               if sline[2] == '_0_':
                   r0 = r0 + int(sline[8])
                   try:
                       if sline[7]=='tcp':
                         r00=r00+int(sline[8])
                   except:
                       continue
               else:
                   r1 = r1 + int(sline[8])
                   try:
                       if sline[7]=='tcp':
                         r11=r11+int(sline[8])
                         time2.append(sline[1])

                   except:
                       continue

           elif sline[0] == 'D':
               dropped += 1
           else:
               print '*'
   except:
              print '0'

time0 = time1[0]
timen = time1[-1]
throughput0=(r11/(float(float(timen)-float(time0))*1000))
throughput1=(r00/(float(float(timen)-float(time0))*1000))




#throughput0=(r1/)
print r0*8
print sent0*8
print r1*8
print sent1*8

print"Data sent by user 0 :",sent00
print"Data sent by user  1 :",sent11
print"Data receiced by user 0 :",r00
print"Data received by user 1 :",r11
print"Total number of packet dropped :",dropped
print "throughput of User 0 :",throughput0
print"throughput of user 1 :",throughput1





#rint(time1)

#Arpit Singh 010810514
#Ankita Chandrachud 010804833
#Program to extract data and calculate the throughput

import re

file = open("s5.tr",'r')
data = file.readlines()[2:]
sent0=0
sent1= 0
r0=0
r1=0
dropped=0
throughput0 = 0
throughput1 = 0
sent00=0
sent11=0
r00=0
r11=0
sent2=0
sent22=0
r2=0
r22=0
time0=[]
time1=[]
time2=[]
time_0=0
time_1=0
time_2=0


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
                         time0.append(sline[1])
                   except:
                         continue

               elif sline[2]=='_1_':
                   sent1 = sent1 + int(sline[8])
                   try:
                       if sline[7]=='tcp':
                         sent11=sent11+int(sline[8])
                         time1.append(sline[1])

                   except:
                       continue
               else:
                   sent2=sent2+int(sline[8])
                   try:
                       if sline[7]=='tcp':
                           sent22=sent22+int(sline[8])
                           time2.append(sline[1])
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
               elif sline[2]=='_1_':
                   r1 = r1 + int(sline[8])
                   try:
                       if sline[7]=='tcp':
                         r11=r11+int(sline[8])
                         time2.append(sline[1])

                   except:
                       continue

               else:
                   r2 = r2 + int(sline[8])
                   try:
                       if sline[7] == 'tcp':
                           r22 = r22 + int(sline[8])
                   except:
                       continue

           elif sline[0] == 'D':
               dropped += 1
           else:
               print '*'
   except:
              print '0'

#time_0 = float(time0[-1])-float(time0[0])
#time_1 = float(time1[-1])-float(time1[0])
#time_2 = float(time2[-1])-float(time2[0])


throughput0=((sent00/(5.971751650-0.507019483))/1000)*8
throughput2=((sent22/(5.992844800-0.507019483))/1000)*8
nt_th=throughput0+throughput1+throughput2


print"Total number of bit sent by user 0 :",sent00
print"Total number of bit sent by user  1 :",sent11
print"Total number of bit sent by user 2 :",sent22
print"Total number of bit received by user 0 :",r00
print"Total number of bit received by user 1 :",r11
print"Total number of bit received by user 2 :",r22
print"Total number of packet dropped :",dropped
print "throughput of User 0 :",throughput0
print"throughput of user 1 : 0"
print"throughput of user 2 :",throughput2
print"nt_th :",nt_th
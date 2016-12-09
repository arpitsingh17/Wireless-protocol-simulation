import re

file = open("10users.tr",'r')
data = file.readlines()[3:]
li = []
datalist ={}
droplist={}
#print datalist[0]


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
throughput = []


for line in data:

   sline = line.split(" ")
   #print sline
   try:
       for node in range(10):
         if sline[0]=='s' and sline[2]==str('_'+str(node)+'_') and sline[7]=='tcp':
            if node in datalist.items():
                datalist[node] += sline[8]
            else:
                datalist[node] = sline[8]
         if sline[0] == 'D' and sline[2] == str('_' + str(node) + '_') and sline[7] == 'tcp':
             if node in datalist.items():
                 droplist[node] += sline[8]
             else:
                 droplist[node] = sline[8]
   except:
        print

print datalist
a=  int(datalist[1])/(11.61-2.5435)
b= int(datalist[2])/(11.956-2.11)
c=  int(datalist[3])/(11.669-3.34)
d=  int(datalist[4])/(11.58-4.54)
e= int(datalist[5])/(11.39-5.51)
f= int(datalist[6])/(11.43-7.03)
g= int(datalist[8])/(11.944-8.12)

total = (a+b+c+d+e+f+g)*8
print "average user throughput",(total/100)/1000
print "network throughput", total/1000


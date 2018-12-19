#!/usr/bin/python
import os
# This will remove the previously processed alert.full file
os.system("rm -f /snort/alert.full")
#create a directory called /snort/alert and put the alert.full file in it.
fhand=open("/snort/alert/alert.full")
l=fhand.readlines()
for index,line in enumerate(l):
  if line.startswith('[**]'):
    line = line.strip('\n')
    x=line

  else:
   if not line.startswith('[**]'):
        line = line.strip('\n')
        y=line

        x=x+y  #adding the second line to the first line x
        z=len(x) # length of concatenated line
        if line.endswith('TcpLen: 20') and z> 250:
           print(x)
           print('\n')
           myfile=open("/snort/alert.full", 'a')
           myfile.write('\n')
           myfile.write(x)
fhand.close()

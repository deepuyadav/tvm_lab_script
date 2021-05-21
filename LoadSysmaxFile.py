#!/usr/bin/env python

import os
import datetime
import time
import shutil

srcPathName ="C:\\SYSMEX_XN550\\"
desFilePath ="Z:\\M18\\"
orgFilePathe="D:\\orgFilePath\\"
faildFilePathe="D:\\faildFilePathe\\"


def parseSysmaxFile(filePath, fileName):
    line_Count=0
    testDate = datetime.date.today()
    #f_file=open(filePathName,'r')
    #line = f_file.readline()
    for line in open(filePath):
        line =line.strip()
        #print ("First Line is: ", line)
        line_Count=(line_Count) + 1
        #print('first_char_line:',line_Count)
        if (line_Count ==2):
            toc=line.split(',')
            VIALID=toc[0]
            TestDate=toc[4]
            TEST=toc[1]
            RESULT=toc[2]
            Date= TestDate.split(' ')
            reqDate=datetime.datetime.strptime(Date[0],'%d-%b-%y') .strftime('%d/%m/%Y')
            print('date: '+reqDate)
            output_file = open(desFilePath+fileName, "w")
            output_file.write('MYTHIC 1;18ST;RESULT\n')
            output_file.write('DATE ;'+reqDate+'\n')
            output_file.write('TIME;'+Date[1]+'\n')
            output_file.write('MODE;NORMAL '+'\n')
            output_file.write('ID;'+VIALID+'\n')
            output_file.write('OPERATOR;\n')
            output_file.write(TEST+';'+RESULT+'\n')

        elif (line_Count > 2):
            toc=line.split(',')
            TEST=toc[1]
            RESULT=toc[2]
            UNIT=toc[3]
            #print('id : ',VIALID+' Test:  '+TEST+' RESULT: '+RESULT+' UNIT: '+UNIT+' TestDate: '+TestDate)
            #print('line: ',line_Count)
            output_file.write(TEST+';'+RESULT+'\n')
          
    #Open output file
    output_file.write('END_RESULT;\n');
    output_file.close();

while 1:
   #check if new file in FilePath
   files = os.listdir(srcPathName)
   for f in files:     #Check if any files are present in the list --
      #Process new file
      absolutefilename =srcPathName + f
      print(f)
      if f[0]== '_':
         shutil.move(srcPathName+f, faildFilePathe)
      else:
          parseSysmaxFile(absolutefilename,f)
          shutil.move(srcPathName+f, orgFilePathe)
   #Wait before next directory check
   time.sleep(30) 

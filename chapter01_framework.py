import os
import sys
import datetime
FunDes = input()
head = '# '+'-'*20+'\n'+\
     '# Function description:\n'+\
     '# '+'-'*20+'\n'+\
     '# Author : Frey Song\n'+\
     '# Emeil : song.fulei@bestv.com.cn\n'+\
     '# '+'-'*20+'\n'

desFile = sys.argv[1]

if os.path.exists(desFile) or not desFile.endswith('.py'):
    print('%s already exsit or is not a Python code file!'%desFile)
    sys.exit()

fp = open(desFile,'w')
today = str(datetime.date.today())
fp.write('# -*- coding:utf-8 -*-\n')
fp.write('# Filename: '+desFile+'\n')
fp.write(head)
fp.write('# Date: '+today+'\n')
fp.write('# '+'-'*20+'\n')
fp.close()
#test
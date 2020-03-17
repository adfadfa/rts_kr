import sys
import time

barWidth = 50 # you can play with this
def updateProgressBar(value):
    line = '\r%s%%[%s]' % ( str(value).rjust(3), '-' * int ((float(value)/100) * barWidth))  
    print (line,sys.stdout.flush())

for i in range(1,101):
    updateProgressBar(i)
    time.sleep(0.05) # do the job here
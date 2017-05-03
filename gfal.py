#!/usr/bin/env python



import gfal2
import time



## Check for  SE (Storage Element)  status module

try:

   ctxt = gfal2.creat_context()
   check = ctxt.listdir("<<URL>>")
   print 'Sucessfully connected to SE'

except gfal2.GError as g:

    print 'Unable to connect to PNNL_SE'
    


## Check the files in the directory of user  module

start_time = time.time()

print 'Copy started ....'

dir = ctxt.listdir("<< Specific URL of the user directory in the Storage Element >>")

for i in range(0,10):
    if "file"+str(i) not in dir:
       params = ctxt.transfer_parameters()
	
       ctxt.filecopy(params, "file:///home/admin/randorm.bin","<<URL of the user directory in the SE "+str(i))

        print 'copy sucess'

    else:
        print 'fail'


end_time = time.time() - start_time

#speed = (/end_time)/1024

print ' total  time : %.2f MB/s' % (end_time)

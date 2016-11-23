from os import remove as removin
from numpy import loadtxt
from os.path import isfile, join

data_path = 'combogpxfiles'

# Having run remove_dup.py this file then removes the duplicate files from your downloaded files.
# It would be more efficient to do this before downloading... but I'm an amature...

with open('nodupexceptions.txt', 'r') as f:
    lines = f.read().split(",")

for i in lines:
    try:
        file = join(data_path,i)
        removin(file)        
        print 'removed ' + i
    except:
        print 'error with ' + i 
from os import remove
from numpy import loadtxt
from os.path import isfile, join

# Occasionally the python script to find routes crashes, so there might be duplicates
# of a particular activity identifier in the list. As the list can be big your not going
# to see it, so this runs through the list and creates a text file that does not have any duplicates.  

with open('exceptions.txt', 'r') as f:
    lines = f.read().split(",")
s = []
for i in lines:
	if i not in s:
		s.append(i)

list = ",".join(str(x) for x in s)
with open("nodupexceptions.txt", "a") as myfile: # saves it to a file (which needs to exist and have '0' in it.
	myfile.write(list)

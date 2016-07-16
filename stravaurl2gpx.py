import urllib2
import urllib
import re
#reads route numbers for a comma separated list.
#The file stravaroutes.txt should have a '0' in it to get
#the comma separations going. Then delete the first '0,'
#in the file before running this script.

from numpy import loadtxt
lines = loadtxt("stravaurls.txt", comments="#", delimiter=",", unpack=False)

#the following gets the route numbers and inserts them into a URL for processing
with open('stravaurls.txt', 'r') as f:
    lines = f.read().split(",")
    
for i in lines:
	try:
		print i
		r = int(i)
		route = str(r)
		finalurl = 'http://raceshape.com/strava.export.php?ride=' + route + '&type=GPX'
		html_content = urllib2.urlopen(finalurl).read()
# this is just some debugging printing, it lets me know progress on screen but
# you can remove the 'print' if you want.
# The rest is getting the filename needed for the save
		print finalurl
		gpxname = i + '.GPX'
# There should be a folder 'stravagpxfiles' created in the folder with this script
		saveloc = "stravagpxfiles/" + gpxname
		print saveloc

		testfile = urllib.URLopener()
		testfile.retrieve(finalurl, saveloc)
	except:
		print "didn't find one"
		pass

import urllib2
import urllib
import re

#reads route numbers for a comma separated list.
#The file routes.txt should have a '0' in it to get
#the comma separations going. Then delete the first '0,'
#in the file before running this script.
from numpy import loadtxt
lines = loadtxt("routes.txt", comments="#", delimiter=",", unpack=False)

#the following gets the route numbers and inserts them into a URL for processing
with open('routes.txt', 'r') as f:
    lines = f.read().split(",")
    #list = lines.split(",")
for i in lines:
	print i
	r = int(i)
	route = str(r)
	finalurl = 'http://www.mikepalumbo.com/MMRConverter/Parser.php?workoutId=' + route
	html_content = urllib2.urlopen(finalurl).read()
# this is just some debugging printing, it lets me know progress on screen but
# you can remove the 'print' if you want.
# The rest is getting the filename needed for the save
	print finalurl
	resulturl = re.search("window.location.href = '(.*)';", html_content)
	resultfilename = re.search("window.location.href = 'http://www.mikepalumbo.com//MMRConverter/(.*)';", html_content)
	print resulturl.group(1)
	print resultfilename.group(1)
	gpxurl = resulturl.group(1)
	gpxname = resultfilename.group(1)
# There should be a folder 'gpxfiles' created in the folder with this script
	saveloc = "gpxfiles/" + gpxname
	print saveloc

	testfile = urllib.URLopener()
	testfile.retrieve(gpxurl, saveloc)
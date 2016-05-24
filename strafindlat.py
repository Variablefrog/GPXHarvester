import urllib2
import re
import time
import sys

# This file searches a range of Strava routes and saves the route identifier of
# any routes id'd as 'Auckland, New Zealand'

for x in range (565537902, 565839316): # 565519386 7:39 AM on Thursday, May 5, 2016 - 565839316 4:54 PM on Thursday, May 5, 2016
        try: # not all pages exist so 'try' is needed to catch errors
                tempurl = "https://www.strava.com/activities/" + str(x)
                finalurl = str(tempurl)
                finalfinalurl = urllib2.urlopen(urllib2.Request(finalurl)).geturl()
                html_content = urllib2.urlopen(finalfinalurl).read()
                content_str = str(html_content)
        
                matches = re.findall('Auckland, New Zealand', content_str);


                if finalurl != finalfinalurl: #this is to catch redirects which seem to be getting the script stuck in a loop
                        print 'redirect in ' + str(x)
                
                elif len(matches) == 0: #if auckland is not found it tells you
                        print 'no in ' + str(x)
                        #print 'nothing in ' + str(x)
                        
                else: #if its found it tells you
                        print 'Found it! My string is in %d' % (x)
                        
                        append_txt = str(x)
                        with open("stravaurls.txt", "a") as myfile: # saves it to a file (which needs to exist and have '0' in it.
                                myfile.write(',' + append_txt)
                                myfile.close()
        except:
                print 'error! ' + str(x)
                pass
5

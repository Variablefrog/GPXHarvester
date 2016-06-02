import urllib2
import re

# This file searches a selection of maymyride urls
# to identify ones centred on a specific GPS coordinate

# This is a window of time of uploads on MMR
# I figured them out manually and it was a pain in the arse
for x in range (1456222129, 1456322129): # 1455222129 2nd May - ???
        
        try: #not every page exists so I needed 'try' to catch errors
                tempurl = "http://www.mapmyride.com/workout/" + str(x)
                finalurl = str(tempurl)
                finalfinalurl = urllib2.urlopen(urllib2.Request(finalurl)).geturl()
                html_content = urllib2.urlopen(finalfinalurl).read()
                content_str = str(html_content)
                
                matches = re.findall('center_lat:', content_str);
                matcheslng  = re.findall('center_lng:', content_str);

                if finalurl != finalfinalurl: #this is to catch redirects which seem to be getting the script stuck in a loop
                        print 'redirect in ' + str(x)

                elif len(matches) == 0: #if auckland is not found it tells you
                        print 'no in ' + str(x)
                        #print 'nothing in ' + str(x)

                else: #if its found it tells you
                        print 'Found lat in %d' % (x)
# this next bit is a little long winded. The gist is MMR's workout don't state
# the name of the city anywhere. So we have to find the latitude and longitude
# of Auckland (approximately -36, 174).

                        start = html_content.find('center_lat')
                        latstart = start + 12
                        latstop = start + 35
                        roughlat = html_content[latstart:latstop]
                        thelat = roughlat.split(",")[0]

                        start_lng = html_content.find('center_lng')
                        lngstart = start_lng + 12
                        lngstop = start_lng + 35
                        roughlng = html_content[lngstart:lngstop]
                        thelng = roughlng.split(",")[0]
                        
# I need to print our the date but you could comment this out

                        finddate = html_content.find('created_date: "')
                        startdate = finddate + 15
                        stopdate = finddate + 25
                        thedate = html_content[startdate:stopdate]
                        
                        latstr = int(float(thelat))
                        latnum = int(latstr)
                        lngstr = int(float(thelng))
                        lngnum = int(lngstr)

# If the lat & long are the same as Auckland, it writes
# the workout number to a text file
# If its not in Auckland, it prints it to CLI

                        if latnum == -36 and lngnum == 174:
                                print 'In AKL ' + str(x) + ' from ' + thedate 
                                append_txt = str(x)
                                with open("mmrurls.txt", "a") as myfile: # this file needs to exist and have '0' in it to start.
                                        myfile.write(',' + append_txt) #adds the route id to a txt file
                        else:
                                print 'Not in AKL ' + str(x) + ' from ' + thedate
        except:
                print 'there was an error!'
                pass

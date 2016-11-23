# GPXHarvester
A Set of Python scripts to gather and visualise gepgraphically specific GPX files from fitness tracker websites Strava and MApMyRide.

This set of files are intended to be deployed in the following order:

strafindlat.py / This file starts wtih defining two numerical values that represent two actual activites on Strava that demark a specific time period. Each upload of an activity to Strava gets a unique URL such as https://www.strava.com/activities/1234567. The script then cycles through all possible activities looking for 'Auckland, New Zealand' and when it finds an activity that was uplaoded from Auckland it saves the unique activity number to a txt file. To run this file you need a text file in the same directory called 'stravaurls.txt' the file should contain the content "o," When the script is finished the stravaurls.txt file will have a list of the relevant strava 'activities' between the two strings that were located in Auckland, New Zealand.

mmr_find_akl.py / This scripts does the same as strafindlat.py but searches mapmyride. Its a bit different as MMR is not as simple as finding 'Auckland, New Zealand' in the html content. So there is a lot of stuff that strips out lat/long data which is how we identify the location of the workout. It finds the latitude and longitude of the centre of the google map used to display the workout. If this corresponds to Auckland it saves it. To run it you need mmrurls.txt in the same folder with "0," in it.

*url2gpx.py / Both of these files load the url.txt files of strava and mapmyride respectively. They then go about downloading the gpx files for each route/workout/activity into a specific folder that must be present (info in comments in the file).

cyclemaps_intimestamp_window.py / This file also needs an 'exceptions.txt' file present with a '0' in it. Essentially it makes a list of file that need to be removed:
- The first try: except: statement will add activity identifiers to the exception.txt file that are for some reason corrupt and cannot be parsed.
- The second time it would add an activity identifier to the exception.txt file is when a point on the gpx route falls outside the timestamps we have identified.

It will also generate an image of the combined paths.

Having identified these exceptions you can then run the remove_dup.py and remove.py and you will have the set of files of activities that occured within the timestamp window. I created this file because people upload gpx files long after their run or cycle. This file helped idenfiy of the 400+ files uploaded in 2016, only 60 were activities that completely happened within the timestamp window.

Take care running the remove_dup.py and remove.py files as they will delete the rest of your GPX files!

remove_dup.py / # Occasionally the python script to find routes crashes, so there might be duplicates of a particular activity identifier in the list. As the list can be big your not going to see it, so this runs through the list and creates a text file that does not have any duplicates it fills an empty nodupexceptions.txt text file with filenames that can be deleted with remove.py 

remove.py / Having run remove_dup.py this file then removes the duplicate files from your downloaded files. It would be more efficient to do this before downloading... but I'm an amateur...

Finally

timestampcyclemap.py / # This script will take all the files in combogpxfiles folder plot them. Then plot minute by minute progress between the two times t_start and t_stop below. It will save out a series of png images suffixed with 001,002 etc. That can then be turned into an mpg or animated gif. If you only run this file it will use all the gpx plotted routes from the 'combogpxfiles' folder as a background, and use only data from within the timestamp window to plot the minute by minute routes happening within that window. But if there are corrupt gpx files it can crash.

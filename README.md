# GPXHarvester
A Set of Python scripts to gather and visualise gepgraphically specific GPX files from fitness tracker websites Strava and MApMyRide.

This set of files are intended to be deployed in the following order:

strafindlat.py / This file starts wtih defining two numerical values that represent two actual activites on Strava that demark a specific time period. Each upload of an activity to Strava gets a unique URL such as https://www.strava.com/activities/1234567. The script then cycles through all possible activities looking for 'Auckland, New Zealand' and when it finds an activity that was uplaoded from Auckland it saves the unique activity number to a txt file. To run this file you need a text file in the same directory called 'stravaurls.txt' the file should contain the content "o," When the script is finished the stravaurls.txt file will have a list of the relevant strava 'activities' between the two strings that were located in Auckland, New Zealand.

mmr_find_akl.py / This scripts does the same as strafindlat.py but searches mapmyride. Its a bit different as MMR is not as simple as finding 'Auckland, New Zealand' in the html content. So there is a lot of stuff that strips out lat/long data which is how we identify the location of the workout. It finds the latitude and longitude of the centre of the google map used to display the workout. If this corresponds to Auckland it saves it. To run it you need mmrurls.txt in the same folder with "0," in it.

*url2gpx.py / Both of these files load the url.txt files of strava and mapmyride respectively. They then go about downloading the gpx files for each route/workout/activity into a specific folder that must be present (info in comments in the file).

from os import listdir
from os import remove
from numpy import loadtxt
import matplotlib.pyplot as plt
from os.path import isfile, join
import gpxpy
import re
import datetime
import dateutil

data_path = 'combogpxfiles'
data = [f for f in listdir(data_path) if isfile(join(data_path,f))]

lat = []
lon = []
t_start = '2016-05-05T00:33:00'
t_stop = '2016-05-05T04:20:00'

fig = plt.figure(facecolor = '0.05')
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_aspect('equal')
ax.set_axis_off()
fig.add_axes(ax)

for activity in data: 
    gpx_filename = join(data_path,activity) 
    gpx_file = open(gpx_filename, 'r')
    try:
        gpx = gpxpy.parse(gpx_file)
    except:
        with open("exceptions.txt", "a") as myfile: # this file needs to exist and have '0' in it to start.
            myfile.write(',' + activity) #adds the route id to a txt file
        print 'added ' + activity
        
    for track in gpx.tracks:
        for segment in track.segments:
            try:
                for point in segment.points:
                    time = point.time.isoformat()
                    if time > t_start and time < t_stop:
                        print 'true ' + activity
                        lat.append(point.latitude)
                        lon.append(point.longitude)
                    else:
                        with open("exceptions.txt", "a") as myfile: # this file needs to exist and have '0' in it to start.
                            myfile.write(',' + activity) #adds the route id to a txt file
                    
            except:
                print 'error'
                pass
                
            plt.plot(lon, lat, color = 'deepskyblue', lw = 0.2, alpha = 0.8)
            lat = []
            lon = []

filename = data_path + '.png'
plt.savefig(filename, facecolor = fig.get_facecolor(), bbox_inches='tight', pad_inches=0, dpi=720)

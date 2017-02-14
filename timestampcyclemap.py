from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import gpxpy
import datetime
import dateutil

# This script will take all the files in combogpxfiles folder plot them
# Then plot minute by minute progress between the two
# times t_start and t_stop below.

# It will save out a series of png images suffixed with 001,002 etc
# That can then be turned into an mpg or animated gif.

data_path = 'combogpxfiles'
data = [f for f in listdir(data_path) if isfile(join(data_path,f))]

# Window of time you need to change the two values below.

t_start = '2016-05-04 19:31:00'
t_stop = '2016-05-05 04:20:00'
pointtime = dateutil.parser.parse (t_start)
form_s_time = dateutil.parser.parse (t_stop)
final_stoptime = form_s_time.replace(second=0)
fident = 000 # this is the start value for the suffix.

# The following two lines are needed to replace the seconds with '0'
# This was necessary (for me) so that at the end time is identified and
# the 'while' condition is met and stops the script
  
newpointtime = pointtime.replace(second=0)
formattedt_stop = final_stoptime.replace(second=0)

while newpointtime != formattedt_stop:

	print newpointtime.isoformat()

	lat = []
	lon = []
	lat1 = []
	lon1 = []

	fig = plt.figure(facecolor = '0.15')
	ax = plt.Axes(fig, [0., 0., 1., 1.], )
	ax.set_aspect('equal')
	ax.set_axis_off()
	fig.add_axes(ax)
	ax.text(0.95, 0.01, newpointtime,
        verticalalignment='top', horizontalalignment='left',
        transform=ax.transAxes,
        color='white', fontsize=15)

	for activity in data:
		gpx_filename = join(data_path,activity)
		gpx_file = open(gpx_filename, 'r')
		try:
		    gpx = gpxpy.parse(gpx_file)
		except:
		    break
		
# This breaks the gpx tracks down

		for track in gpx.tracks:
			for segment in track.segments:
				for point in segment.points:
					time = point.time.isoformat()
					firstwin = str(newpointtime.isoformat()[:16])
					window = firstwin
					
# This draws the minute progress

					if window in time :
						lat1.append(point.latitude)
						lon1.append(point.longitude)
						plt.plot(lon1, lat1,'ro', markersize=3)
				lat1 = []
				lon1 = []
# This draws the entire routes in entirety. 
		for track in gpx.tracks:
			for segment in track.segments:
				for point in segment.points:
					lat.append(point.latitude)
					lon.append(point.longitude)
		plt.plot(lon, lat, color = 'deepskyblue', lw = 0.2, alpha = 0.8, zorder=0)
		lat = []
		lon = []

# This saves out the figure and adds one to the minute count and the file suffix.
	fident3dig = format(fident, "03d")
	fidentstr = str(fident3dig)
	filename = data_path + fidentstr + '.png'
	#plt.imshow(img, alpha = 0.8, zorder=0)
	plt.savefig(filename, facecolor = fig.get_facecolor(), bbox_inches='tight', pad_inches=0, dpi=720)
	plt.close(fig)
	newpointtime = newpointtime + datetime.timedelta(0,60)
	fident = fident + 1

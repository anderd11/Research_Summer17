import matplotlib.pyplot as plt
from csv import reader
import math as m
#from astropy import coordinates as coord
#from astropy import units as u

'''
need to convert coordinates
required before zooming in on image
'''

with open('FinalQuery06282017.csv', 'r') as f:
    data = list(reader(f))

#print(data[0])      #this line prints the first column of data in our 'table'
#print(data[1])      #this line prints the second column of data in our 'table'

# these next several lines create lists of each stat
objID = [i[0] for i in data]
ra = [i[1] for i in data]
dec = [i[2] for i in data]
l = [i[3] for i in data]
b = [i[4] for i in data]
psfMag_u = [i[5] for i in data]
psfMag_r = [i[6] for i in data]
psfMag_i = [i[7] for i in data]
psfMag_g = [i[8] for i in data]
psfMag_z = [i[9] for i in data]
psfMagErr_u = [i[10] for i in data]
psfMagErr_r = [i[11] for i in data]
psfMagErr_i = [i[12] for i in data]
psfMagErr_g = [i[13] for i in data]
psfMagErr_z = [i[14] for i in data]
extinction_u = [i[15] for i in data]
extinction_r = [i[16] for i in data]
extinction_i = [i[17] for i in data]
extinction_g = [i[18] for i in data]
extinction_z = [i[19] for i in data]
loggadop = [i[21] for i in data]
loggadopunc = [i[22] for i in data]
fehadop = [i[23] for i in data]
fehadopunc = [i[24] for i in data]
elodiervfinal = [i[25] for i in data]
elodiervfinalerr = [i[26] for i in data]

#print(data[0])

# creates scatter plot of star postions
# removes strings from list to plot
ra.pop(0)
dec.pop(0)

plt.scatter(ra, dec, s= 0.1, label= 'Positions of Stars')

plt.xlabel('Right Ascension')
plt.ylabel('Declination')

# sets bounds for the x axis and y axis
plt.xlim([m.floor(min(ra)),m.ceil(max(ra))])
plt.ylim([m.floor(min(dec)),m.ceil(max(dec))])

plt.show()

'''
could have propblem with lines 59 and 60
using functions that belong to floats
what if the min/max isn't a float
'''
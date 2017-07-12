import matplotlib.pyplot as plt
from csv import reader

with open('Trying3.csv', 'r') as f:
    data = list(reader(f))

#print(data[0])      #this line prints the first column of data in our 'table'
#print(data[1])      #this line prints the second column of data in our 'table'

# these next several lines create lists of each stat
objID = [i[0] for i in data]
ra = [i[1] for i in data]
dec = [i[2] for i in data]
psfMag_u = [i[3] for i in data]
psfMag_r = [i[4] for i in data]
psfMag_i = [i[5] for i in data]
psfMag_g = [i[6] for i in data]
psfMag_z = [i[7] for i in data]
psfMagErr_u = [i[8] for i in data]
psfMagErr_r = [i[9] for i in data]
psfMagErr_i = [i[10] for i in data]
psfMagErr_g = [i[11] for i in data]
psfMagErr_z = [i[12] for i in data]
extinction_u = [i[13] for i in data]
extinction_r = [i[14] for i in data]
extinction_i = [i[15] for i in data]
extinction_g = [i[16] for i in data]
extinction_z = [i[17] for i in data]

# creates scatter plot of star postionsSS
# removes strings from list to plot
ra.pop(0)
dec.pop(0)

plt.scatter(ra, dec, label= 'Positions of Stars')

plt.xlabel('Right Ascension')
plt.ylabel('Declination')

plt.show()
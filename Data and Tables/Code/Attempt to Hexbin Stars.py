import numpy as np
import matplotlib.pyplot as plt
from csv import reader

with open('FinalQuery06282017.csv', 'r') as f:
    data = list(reader(f))


'''
having trouble understanding the syntax to graph MY data
ncol must mean number of graphs/charts/columns but I can't get it to only show one
'''
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

# creates scatter plot of star postions
# removes strings from list to plot
ra.pop(0)
dec.pop(0)

#plt.scatter(ra, dec, s= 0.1, label= 'Positions of Stars')

#plt.xlabel('Right Ascension')
#plt.ylabel('Declination')

#plt.show()





np.random.seed(0)
n = 100000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)

## naming variables
#xmin = x.min()
#xmax = x.max()
#ymin = y.min()
#ymax = y.max()

fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(10, 6))

# determines intervals and width of axes (left is interval, right is width of charts)
fig.subplots_adjust(hspace=0.5, left=0.07, right=0.93)

#'''
#this section will build the first chart
#'''
## don't know, don't mess with
#ax = axs[0]

## chooses color and size of chart
#hb = ax.hexbin(x, y, gridsize=50, cmap='Blues_r')
#ax.axis([xmin, xmax, ymin, ymax])

## title of first chart
#ax.set_title("Hexagon binning")

## adds side bar to show color scale
#cb = fig.colorbar(hb, ax=ax)

## label of first color scale bar
#cb.set_label('counts')



'''
this section will build the second chart
'''
ax = axs[0]

# chooses color and size of chart
hb = ax.hexbin(ra, dec, gridsize=500, cmap='inferno')

# should but don't know, learn!
#ax.axis([xmin, xmax, ymin, ymax])

# title of second chart
ax.set_title("With a log color scale")

# don't know, don't touch
cb = fig.colorbar(hb, ax=ax)

#label of second color scale bar
cb.set_label('log10(N)')


'''
this last line plots both charts
'''
plt.show()
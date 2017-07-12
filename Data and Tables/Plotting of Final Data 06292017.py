import matplotlib.pyplot as plt
from csv import reader
import math as m
#from astropy import coordinates as coord
#from astropy import units as u

with open('NoSpecGrav.csv', 'r') as f:
    data = list(reader(f))

#print(data[0])      #this line prints the first column of data in our 'table'
#print(data[1])      #this line prints the second column of data in our 'table'

# these next several lines create lists of needed stats
objID = [i[0] for i in data]
l = [i[1] for i in data]
b = [i[2] for i in data]
ra = [i[3] for i in data]
dec = [i[4] for i in data]


# creates scatter plot of star postions
# removes strings from list to plot
l.pop(0)
b.pop(0)

plt.scatter(l, b, s= 0.1, label= 'Positions of Stars')

plt.xlabel('l')
plt.ylabel('b')

# sets bounds for the x axis and y axis
plt.xlim([0,160])
plt.ylim([-40,40])

plt.show()
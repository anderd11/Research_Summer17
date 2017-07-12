import matplotlib.pyplot as plt
from csv import reader
import math as m

# reads file and creates list of data
with open('DatawithoutSpectraorGravityCut.csv','r') as f:
    data = list(reader(f))
    
#print(data[0])

# creates a list of each stat
objID = [i[0] for i in data]
l = [i[1] for i in data]
b = [i[2] for i in data]
ra =[i[3] for i in data] 
dec = [i[4] for i in data]
psfMag_u = [i[5] for i in data]
psfMag_r = [i[6] for i in data]
psfMag_i = [i[7] for i in data]
psfMag_g = [i[9] for i in data]
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


## creates scatter plot of stars in data
# removes title from list so we can plot
l.pop(0)
b.pop(0)

plt.scatter(l, b, s= 0.1, label = 'Star Positions: No Restrictions')
plt.xlabel('l')
plt.ylabel('b')

# sets bounds for x axis and y axis
plt.xlim(m.floor(min(l)),m.ceil(max(l)))
plt.ylim(m.floor(min(b)),m.ceil(max(b)))

plt.show()
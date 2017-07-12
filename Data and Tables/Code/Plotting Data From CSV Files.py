import matplotlib.pyplot as plt
from csv import reader

with open('Trying.csv', 'r') as f:
    data = list(reader(f))

print(data[0])      #this line prints the first column of data in our 'table'
print(data[1])      #this line prints the second column of data in our 'table'

objID = [i[0] for i in data]
ra = [i[1] for i in data]
psfMag_u = [i[0] for i in data]
psfMag_r =
psfMag_i =
psfMag_g =
psfMagErr_u =
psfMagErr_r =
psfMagErr_i =
psfMagErr_g =
extinction_u =
extinction_r =
extinction_i =
extinction_g =
extinction_z =

'''
missing psfMag_z and
missing psfMagErr_z
don't know why
'''
plt.plot(data[1], data[2], label= 'try')
plt.xlabel('column 2')
plt.ylabel('column 3')
plt.title('trying')
plt.show()
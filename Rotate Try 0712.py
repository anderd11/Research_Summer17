import matplotlib.pyplot as plt
from csv import reader
import numpy as np
import math


# function to rotate coordinates     
def rotate(a, b, angle):

    x = [80.297,-24.52]
    y = [a, b]

    xx = y[0]-x[0]
    yy = y[1]-x[1]

    newx = (xx*math.cos(angle)) - (yy*math.sin(angle))

    newy = (xx*math.sin(angle)) + (yy*math.cos(angle))

    newx+= x[0]

    newy+= x[1]

    return newx,newy

# opens and reads data from csv file
with open('4milNoSpec.csv', 'r') as f:
    data_1 = list(reader(f))
    
with open('4milUpper.csv','r') as j:
    data_2 = list(reader(j))
    
# stores variables needed for plotting
objID_1 = [i[0] for i in data_1]
l_1 = [i[1] for i in data_1]
b_1 = [i[2] for i in data_1]
# storing more variables from separate query to cover more points
objID_2 = [i[0] for i in data_2]
l_2 = [i[1] for i in data_2]
b_2 = [i[2] for i in data_2]

# removes strings from lists
l_1.pop(0)
b_1.pop(0)
l_2.pop(0)
b_2.pop(0)

# adds data points from other query
l_1.extend(l_2)
b_1.extend(b_2)

# lists to store shifted coordinates in
new_l = []
new_b = []

# shifts each coordinate and stores it's new value
for i in range(len(l_1)):
    h, k = rotate(float(l_1[i]), float(b_1[i]), 75.96375653)
    new_l.append(h)
    new_b.append(k)
            
#print(new_l[523], new_b[523])

# builds rotated plot of stars
plt.scatter(new_l, new_b, s = 0.1, label = 'Rotated Star Positions')
plt.xlabel('l\'')
plt.ylabel('b\'')
plt.xlim(min(new_l), max(new_l))
plt.ylim(min(new_b), max(new_b))
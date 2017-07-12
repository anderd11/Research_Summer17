import matplotlib.pyplot as plt
from csv import reader
import numpy as np
from math import *


# function to plot line based on slope and y-intercept
def abline(slope, intercept):
     axes = plt.gca()
     x_vals = np.array(axes.get_xlim())
     y_vals = (slope * x_vals) + intercept
     plt.plot(x_vals, y_vals, '--', color='red')
     
# function to rotate coordinates     
def rotate(a, b, angle):

     x = [80.297,-24.52]
     y = [a, b]

     xx = y[0]-x[0]
     yy = y[1]-x[1]

     newx = (xx*cos(radians(angle))) - (yy*sin(radians(angle)))

     newy = (xx*sin(radians(angle))) + (yy*cos(radians(angle)))

     newx+= x[0]

     newy+= x[1]

     return newx,newy

# plotting points where expected stream is located
plt.scatter([69], [-27], marker='o', s=5, color='red')
plt.scatter([89], [-22], marker='o', s=5, color='red')
abline(0.25, -44.25)

# converting old coordinates using rotate function
h, j = (rotate(69, -27, 75.96375653))
s, t = (rotate(89, -22, 75.96375653))

# plots new coordinates on graph
plt.scatter(h, j)
plt.scatter(s, t)

# draw line to check if new points are vertical
plt.plot((h,s),(j,t), 'red')

# print both new x coordinates to see if they are actually vertical
print(h, s)
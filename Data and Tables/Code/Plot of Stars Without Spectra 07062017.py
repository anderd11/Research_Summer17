import matplotlib.pyplot as plt
from csv import reader
import numpy as np
'''
the line in this program uses y = mx + b
we create two lines based on the points (separately)
this is because the image from Hélio only looks MOSTLY linear
'''
# function to plot line based on slope and y-intercept
def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = (slope * x_vals) + intercept
    plt.plot(x_vals, y_vals, '--', color='red')

# opens and reads data from csv file
with open('4milNoSpec.csv', 'r') as f:
    data = list(reader(f))
    
# stores variables needed for plotting
objID = [i[0] for i in data]
l = [i[1] for i in data]
b = [i[2] for i in data]

# removes strings from list so we can plot
l.pop(0)
b.pop(0)

# creates scatter plot of star positions
plt.scatter(l, b, s = 0.1, label = 'Position of Stars')
plt.xlabel('l')
plt.ylabel('b')

# sets bounds for the x axis and y axis
plt.xlim([65,95])
plt.ylim([-30,-20])

# plotting points where expected stream is located
plt.scatter([69], [-27], marker='o', s=5, color='red')
plt.scatter([89], [-22], marker='o', s=5, color='red')
#abline(0.3, -47.7)
#abline(0.3, -48.7)
abline(0.25, -44.25)
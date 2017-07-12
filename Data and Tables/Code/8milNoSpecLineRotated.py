import matplotlib.pyplot as plt
from csv import reader
import numpy as np

# function to plot line based on slope and y-intercept
def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = (slope * x_vals) + intercept
    plt.plot(x_vals, y_vals, '--', color='red')

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

# creates scatter plot of star positions
plt.scatter(l_1, b_1, s = 0.1, label = 'Position of Stars')
plt.xlabel('l\'')
plt.ylabel('b\'')

# sets bounds for the x axis and y axis
plt.xlim([65,95])
plt.ylim([-30,-20])

# plotting points where expected stream is located
plt.scatter([69], [-27], marker='o', s=5, color='red')
plt.scatter([89], [-22], marker='o', s=5, color='red')
abline(0.25, -44.25)
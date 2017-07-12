import matplotlib.pyplot as plt
from csv import reader
import numpy as np

with open('4milNoSpec.csv', 'r') as f:
    data_1 = list(reader(f))
    
with open('3milUpper.csv','r') as j:
    data_2 = list(reader(j))
    

print(data_1)
print(data_2)
## stores variables needed for plotting
#objID_1 = [i[0] for i in data_1]
#l_1 = [i[1] for i in data_1]
#b_1 = [i[2] for i in data_1]
## storing more variables from separate query to cover more points
#objID_2 = [i[0] for i in data_2]
#l_2 = [i[1] for i in data_2]
#b_2 = [i[2] for i in data_2]

## removes strings from lists
#l_1.pop(0)
#b_1.pop(0)
#l_2.pop(0)
#b_2.pop(0)

## adds data points from other query
#l_1.append(l_2)
#b_1.append(b_2)

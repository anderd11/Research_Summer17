import math
import matplotlib.pyplot as plt

def rotate(a, b, d_angle):
    theta = math.radians(d_angle)
    
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    
    new_x = a[0] + ((dx*math.cos(theta) - dy*math.sin(theta)))
    new_y = a[1] + ((dx*math.sin(theta) + dy*math.cos(theta)))
    return new_x, new_y

one = (5, 5)

two = (0, 0)

hope = rotate(one, two, 90)
plt.plot(one, two, 'green')
plt.plot(hope[0], hope[1], 'purple')
plt.scatter(one[0], one[1], 'purple')
plt.scatter(two[0], two[1], 'blue')

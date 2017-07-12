import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
n = 100000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)

# naming variables
xmin = x.min()
xmax = x.max()
ymin = y.min()
ymax = y.max()

fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(7, 4))

# determines intervals and width of axes (left is interval, right is width of charts)
fig.subplots_adjust(hspace=0.5, left=0.07, right=0.93)

'''
this section will build the first chart
'''
# don't know, don't mess with
ax = axs[0]

# chooses color and size of chart
hb = ax.hexbin(x, y, gridsize=50, cmap='Blues_r')
ax.axis([xmin, xmax, ymin, ymax])

# title of first chart
ax.set_title("Hexagon binning")

# adds side bar to show color scale
cb = fig.colorbar(hb, ax=ax)

# label of first color scale bar
cb.set_label('counts')



'''
this section will build the second chart
'''
ax = axs[1]

# chooses color and size of chart
hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')

# should but don't know, learn!
ax.axis([xmin, xmax, ymin, ymax])

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


import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-20,20,1000)

# the function, which is y = x^2 here
y = -0.5*x-3
y1= x**2
y2= 4*x*(1-x)

# setting the axes at the centre
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')

# plot the function
plt.ylim([-20, 20])

plt.plot(x,y, 'r')
plt.plot(x,x, 'b')
plt.plot(x,y1, 'g')
plt.plot(x,y2, 'y')

# show the plot
plt.show()


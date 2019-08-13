import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(100000.0)
y = x**2+5

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='X', ylabel='Y',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()

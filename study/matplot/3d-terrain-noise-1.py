# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
import random

from pynoise import perlin
from opensimplex import OpenSimplex

def remap(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

scl = 50
w = 1000
h = 1000
cols = w//scl
rows = h//scl



X = np.linspace(0.0,w,num=cols)
Y = np.linspace(0.0,h,num=rows)
X, Y = np.meshgrid(X, Y)
x = X.flatten()
y = Y.flatten()
print(len(x))

smpx = OpenSimplex(seed=10)
prln = perlin.Perlin(frequency=50)
#terrain = np.random.randint(-10,10,(cols,rows))
#Z = [smpx.noise2d(x[i]*3,y[i]*3) for i in range(len(x))]

#Z = [remap(prln.value(i*0.1,i*0.1,0.0),0,1,-100,100) for i in range(len(x))]

Z=[]
yoff=0
for i in range(rows):
    xoff=0
    for j in range(cols):
        Z.append(remap(smpx.noise2d(xoff,yoff),-1,1,-300,300))
        xoff+=0.2
    yoff+=0.2



z=Z
print(Z)
#z = terrain.flatten()
#z = [0 for i in range(len(x))]

fig = plt.figure()
ax = fig.gca(projection='3d')
scale_x,scale_y,scale_z=1,1,0.5
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([scale_x, scale_y, scale_z, 1]))

ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()

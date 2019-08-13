import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


with open('python/misc/imdb.txt','r') as f:
    data = f.read().split('\n')
    d = {}
    for e in data:
        name = e[3:e.index('(')]
        year = e[e.index('(')+1:-1]
        if year in d:
            d[year]+=1
        else:
            d[year]=1


d = sorted(d.items())

x = np.array([x[1] for x in d])
y = np.array([x[0] for x in d])

plt.barh(y, x, align='center', alpha=0.5)
#plt.yticks(y_pos, y)


plt.show()
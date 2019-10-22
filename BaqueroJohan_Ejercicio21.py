import numpy as np
import matplotlib.pylab as plt

t = np.linspace(0,4*np.pi,100)
y = np.sin(t)
plt.plot(t,y,color ="black")
plt.show()
plt.savefig("Función seno")
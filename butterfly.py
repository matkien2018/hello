import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi,300)
x = np.sin(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t))
y = np.cos(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t))

fig = plt.figure(figsize=(6,6))
fig.canvas.manager.set_window_title('Butterfly Curve')

plt.plot(x,y,color='purple',linewidth=2)
#plt.plot(-x,y,color='orange',linewidth=2)

plt.title('Beautiful Butterfly Curve',fontsize=20)
plt.axis('equal')
plt.axis('off')
plt.show()
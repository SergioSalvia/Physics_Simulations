import numpy as np
import matplotlib.pyplot as plt
from random import uniform
from math import sqrt
import matplotlib.animation as animation

# Frame updating
def update_plot(frame, P, plot, jump):
    plot[0].remove()
    n = int(frame*jump)
    ax.set_title('$\pi$ =' + str(round(P[n,2],4)))
    plot[0] = ax.scatter(P[1:n,0],P[1:n,1],s = 0.001, color = 'blue')
    
    
# Figure definitions
fig, ax = plt.subplots(1,1,figsize=(5,5))
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)

# Plot circle
x = np.linspace(-1.0, 1.0, 100)
y = np.linspace(-1.0, 1.0, 100)
X, Y = np.meshgrid(x,y)
C = X**2 + Y**2 - 1
ax.contour(X,Y,C,[0])

# Monte Carlo
N = 1000000
# Matrix to store points for later picture
P = np.zeros((N, 3))
p_in = 0
for i in range(1,N):
    v = [uniform(-1,1),uniform(-1,1)]
    dC = v[0]**2+v[1]**2 
    p_in = p_in + int(dC<=1)
    P[i,0] = v[0]
    P[i,1] = v[1]
    P[i,2] = 4*p_in/i
    
    
# Initial point
plot = [ax.scatter(P[0,1],P[0,2],s = 0.001)]
    
nmax = 50
jump = N/nmax
animate = animation.FuncAnimation(fig, update_plot, nmax, fargs=(P, plot, jump))
animate.save('MC.gif',writer='imagemagick')


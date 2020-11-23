#!/usr/bin/env python
# coding: utf-8

# ### OBE with time dissipation
# In this notebook we can play around with the evolution of Bloch vectors in the Bloch sphere. For this, the programme integrates numerically the OBE. Then we represent in an animation the Bloch sphere, the Bloch vector (orange), the evolution of populations (projection on the $s_3$ axis, in green) and the trajectory of the vector during the tive evolution (red).
# 
# The variables we may want to change are:
# 
# Omega = $\Omega_1$
# 
# Delta = $\Delta$
# 
# gamma = $\gamma$
# 
# 
# We also suppose that there are no collisions, that is $\Gamma = 2\gamma$. This can be easily changed. The initial state of the Bloch vector is denoted by the variable s0 that can also be changed.

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.animation as animation
from scipy.integrate import odeint


# This block is just information for the plot and animation.
#---------------------------------------------------------------------------------------------------

# Animation function. It gives every frame and plots the elements plot[i].
# The function .remove() cleans the previous frame so as to avoid overlapping.

def update_plot(frame, v, plot):
    plot[0].remove()
    plot[1].remove()
    plot[0] = ax.quiver( 0, 0, 0, s[frame,0], s[frame,1], s[frame,2],  linewidth = 3.0, color = "orange")
    plot[1] = ax.quiver( 0, 0, 0, 0, 0, s[frame,2],  linewidth = 3.0, color = "green")

# Figure definitions
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(-1,1)
ax.view_init(30, 45)

# Definition of the Bloch sphere and the axis
# Sphere
u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:30j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color = "b", linewidth = .25)
# Axis
ax.plot([0,1],[0,0],[0,0], color = 'black')
ax.plot([0,0],[0,1],[0,0], color = 'black')
ax.plot([0,0],[0,0],[0,1], color = 'black')

#---------------------------------------------------------------------------------------------------

# Here we define the physical problem
#---------------------------------------------------------------------------------------------------

# Definition of the OBE
def OBE(s, t, Omega, Delta, gamma, Gamma):

    s1, s2, s3 = s
    dsdt = [Delta*s2 - gamma*s1,
            -Delta*s1 - Omega*s3 - gamma*s2,
            Omega*s2 - Gamma*(1+s3)]
    
    return dsdt

# Values given for the parameters
Omega = 2
Delta = 0
gamma = 0.3
Gamma = 2*gamma

# This defines the number of frames (nmax) and time duration (T). 
nmax = 100
T = 10
t = np.linspace(0,T,nmax)

# Now we define the initial condition s0 and then integrate the OBE
s0 = [0, 0, 1]
s = odeint(OBE, s0, t, args = (Omega, Delta, gamma, Gamma))

#---------------------------------------------------------------------------------------------------


# Again this is only ploting information
#---------------------------------------------------------------------------------------------------

# Trajectory of the vector in s-space
ax.plot(s[:,0],s[:,1],s[:,2], color = 'red')

# Initial frame
plot = [ax.quiver( 0, 0, 0, s[0,0], s[0,1], s[0,2],  linewidth = 3.0, color = "orange"),
        ax.quiver( 0, 0, 0, 0, 0, s[0,2],  linewidth = 3.0, color = "green")]

# Animation
animate = animation.FuncAnimation(fig, update_plot, nmax, fargs=(v, plot))

#---------------------------------------------------------------------------------------------------
# Saving. You can change the name of the file. 

# To generate a gif we need to install imagemagick (free software). Then use the following line
animate.save('OBE.gif',writer='imagemagick')

# If we don't want to download imagemagick then we can just generate a mp4 file
#animate.save('OBE.mp4', writer = None)
plt.show()


# In[ ]:





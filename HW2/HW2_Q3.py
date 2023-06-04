from mpl_toolkits import mplot3d
import matplotlib.tri as mtri
import numpy as np
import matplotlib.pyplot as plt




R = 4
r = 1

theta = np.linspace(0, 2*np.pi,20,endpoint=True)
phi = np.linspace(0, 2*np.pi,20,endpoint=True)

#mesh the phi and theta 1D-->2D. Then change them back to 1D
phi, theta = np.meshgrid(phi, theta)
phi, theta = phi.flatten(), theta.flatten()
print(phi)
print(theta)
#eq. from hw
x = (R+r*np.cos(theta))*np.cos(phi)
y = (R+r*np.cos(theta))*np.sin(phi)
z = r*np.sin(theta)

#change the triangulation from x,y,z to phi, theta
tri = mtri.Triangulation(phi, theta)

#visualize the plot in 3d
ax = plt.axes(projection='3d')
#change initial orientation
ax.view_init(20,270)
ax.set_zlim(-4,4)
ax.plot_trisurf(x,y,z, cmap = 'jet', triangles = tri.triangles)



import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

S = np.array([[2,-1,-1],[1,0,2],[2,1,0]])

# Data for three-dimensional points
zdata = np.array([1,2,-1,3,2,1,-3,0,-1,1])
xdata = np.array([0,1,2,0,1,-1,1,-4,3,0])
ydata = np.array([-1,-1,0,4,-2,-2,1,1,1,1])

points = np.array([[0,1,2,0,1,-1,1,-4,3,0],[-1,-1,0,4,-2,-2,1,1,1,1],[1,2,-1,3,2,1,-3,0,-1,1]])

# Data for vectors and coloring:

# Color by azimuthal angle
c = np.arctan2(xdata, ydata)
# Flatten and normalize
c = (c.ravel() - c.min()) / c.ptp()
# Repeat for each body line and two head lines
c = np.concatenate((c, np.repeat(c, 2)))
# Colormap
c = plt.cm.hsv(c)

points_new_basis = np.zeros((3,len(xdata)))

# Adding vectors
for i in range(0,len(xdata)):
    # ax.quiver(0, 0, 0, xdata[i], ydata[i], zdata[i], colors=c, arrow_length_ratio=0.1)
    # print(inv(S),points[:,i])
    # points_new_basis[:,i] = inv(S) * points[:,i].T
    points_new_basis[:,i] = inv(S).dot(points[:,i])
    # ax.quiver(0, 0, 0, points_new_basis[0,i], points_new_basis[1,i], points_new_basis[2,i], colors=c, arrow_length_ratio=0.1)

print("new", points_new_basis)

for i in range(0,len(points_new_basis[0,:])):
    a = np.array([0,0,0])
    dist = np.linalg.norm(a-points_new_basis[:,i])
    print("dist for index: ",i,"dist: ", dist)

ax.set_xlim([-3.5, 3.5])
ax.set_ylim([-3.5, 3.5])
ax.set_zlim([-3.5, 3.5])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# ax.scatter3D(xdata, ydata, zdata, c=zdata)
ax.scatter3D(points_new_basis[0,:], points_new_basis[1,:], points_new_basis[2,:], c=zdata)


plt.title('3D Points Plot')

plt.show()
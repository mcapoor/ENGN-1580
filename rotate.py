import numpy as np 
import matplotlib.pyplot as plt

n = 100
x = np.linspace(0, n, n)
y = np.linspace(0, n, n)


phi = np.radians(30) 
R = np.array([[np.cos(phi), -np.sin(phi)],
              [np.sin(phi),  np.cos(phi)]])

X, Y = np.meshgrid(x, y)
Xn, Yn = np.meshgrid(x, y)

for i in range(n):
    for j in range(n):
        [Xn[i, j], Yn[i, j]] = np.dot(R, [X[i, j], Y[i, j]])

fig, ax = plt.subplots()
plt.grid()

ax.scatter(X, Y, c='b', s=1)
ax.scatter(Xn, Yn, c='g', s=1)

plt.show()
import numpy as np

A = np.array([[3,-1,-1],
              [-1,4,-1],
              [-1,-1,3]])
w = np.array([[5],
              [5],
              [0]])

print(np.linalg.solve(A,w))

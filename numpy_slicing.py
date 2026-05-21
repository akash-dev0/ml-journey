import numpy as np
a = np.array([10, 20, 30, 40, 50])
print(a[0])
print(a[-1])
print(a[1:4])
print(a[:3])
print(a[2:])

b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(b[0])
print(b[1][2])
print(b[:,1])
print(b[0:2, 1:3])

print(np.zeros((3, 4)))
print(np.ones((2, 3)))
print(np.arange(0, 10, 2))
print(np.random.randint(0, 100, (3, 3)))
print(np.random.rand(3, 3))

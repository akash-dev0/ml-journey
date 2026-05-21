my_list = [1, 2, 3, 4, 5]

import numpy as np 
my_array = np.array([1, 2, 3, 4, 5])

print(my_list)
print(my_array)

print(my_list * 2) ## repeated the list twice!
print(my_array * 2) ## multiplied every number by 2!

print(my_array + 10)

a = np.array([1, 2, 3, 4, 5])
print(a)
print(a.shape)

b = np.array([[1,2,3],
              [4,5,6]])
print(b)
print(b.shape)
print(b.ndim)
print(b.dtype)
print(b.size)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(np.dot(a, b))


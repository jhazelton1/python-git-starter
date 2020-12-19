import numpy as np

a = np.array([1,2,3], dtype='int16')

print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]], dtype='int16')


print(a.size)
print(a.itemsize)

print('b: ' + str(b))
print(b.ndim)
print(b.shape)
print(b.dtype)
print(b.size)
print(b.itemsize)
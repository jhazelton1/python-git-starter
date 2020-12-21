import numpy as np

a = np.array([1,2,3], dtype='int16')

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]], dtype='int16')

# print(a)
# print(a.size)
# print(a.itemsize)

# print('b: ' + str(b))
# print(b.ndim)
# print(b.shape)
# print(b.dtype)
# print(b.size)
# print(b.itemsize)

c = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
# print(c.shape)
# print(c)
# print(c[1,5])
# print(c[0, :])
# print(c[:, 2])

# c[1,0] = 1337
# print(c)

# c[:,2] = 1337
# print(c)

# c[:,2] = [88, 99]
# print(c)

# d = np.zeros((4, 3, 3))
# print(d)

# print(np.full((4,2,3), 1337))

# print(np.full_like(d, 1336))

# print(np.random.randint(9, size=(3,3)))

matrix = np.ones((5,5), dtype=int)
maxtrix_replacement = np.zeros((3,3), dtype=int)

maxtrix_replacement[1,1] = 9
matrix[1:4, 1:4] = maxtrix_replacement


print(matrix)



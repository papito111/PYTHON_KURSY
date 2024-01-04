import numpy as np


array = np.arange(1000)
# print(array.size*array.itemsize)
a1 = np.array([1, 2, 3])
a2 = np.array([2, 4, 1])
a = a1 * a2
# print(a)
b = np.array([[2, 2, 10], [11, 6, 3], [8, 5, 2], [7, 6, 92]], dtype=np.float32)
print(b)
print(b.ndim)
print(b.itemsize)# wpływa na to dtype nha końcu
print(b.shape)# wymairy tablicy (liczba elementów na wielkość elementu
c = np.arange(1, 10, 2)
print(c)
d = np.linspace(0, 5, 11)
# print(d)
e = b.ravel()
print(e)# wypłaszcza nam tablice do jednego wymiaru
g = np.sqrt(b)
print("min:", b.min(), "max:", b.max(), "suma wyrazów:", b.sum(axis=1), g)# zamiana axis 1 na 0 daje liczenia sumy w zależnosci od któego wymiaru patrzymy
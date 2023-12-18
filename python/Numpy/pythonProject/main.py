import numpy as np

"""
#print(a)
# slicing
# print(a[0:3])
# print(a[-1])
# print(sum(a[0:3, 1]))
for cell in a.flat:
    print(cell)
    
for row in a:
    print(row)
    
c = np.vstack((a, b))# laczenie dwoch tabel mozna dac hstack po drugim wymiarze sie dodaje
#for row in c:
   # print(row)
result = np.vsplit(c,3)
print(result[0])# dzielimy na 3 czesci i potem kazda z tych cześci ma swoj indeks
print(result[1])
print("\n",c)

d = np.arange(12).reshape(3,4)
#print(d)
e = d > 5
#print(e)
print(d[e]) # w e mamy oznaczony warunek on nam wypisuje ile jest tych wyrazów

print(len(d[e])) # tyle jest wyrazow wwiekszych od 5
f = d < 4
d[f]=-1
print(d)
"""
a = np.arange(10)
b = np.array([1, 3, 3, 6, 1, 2])
g = np.array([1, 2, 1, 1, 1, 2])
c = np.array([[2, 2], [3, 4], [9, 6]])
d = np.array([[1, 3], [3, 6], [1, 2]])
e = np.array([[2, 2, 1], [3, 4, 2], [9, 6, 3]])
f = np.array([[1, 3, 2], [3, 6, 1], [1, 2, 1]])
z = b * g
result = np.hsplit(b,3)
print(result[1])
print("\n\n", a, "\n\n\n", b, "\n\n\n", c, "\n\n\n", d, "\n\n\n", e, "\n\n\n", f, "\n\n\n", z, "\n\n\n", result)
mnozenie = np.matmul(c,c.T)# np. matmul mnozy macierze, kolumny = wiersze, roznicą miedzy znakiem * jest to że tam sie mnozy element po elemencie
print(c)# operator .t daje transpozycje
print(c.T)
print(mnozenie)
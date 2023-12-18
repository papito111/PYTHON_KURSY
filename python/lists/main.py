zarobki1 = [2200,2350,2600,2130,2190]
print(zarobki1[1] - zarobki1[0])# 1
quarter = zarobki1[:3]
print(sum(quarter))
print(2000 in zarobki1)
zarobki2 = [1980]
zarobki = zarobki1 + zarobki2
print(zarobki)
zarobki[4] = zarobki[4] + 200
print(zarobki)
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
nowy_heros = ['black panther']
#heros += nowy_heros append daje na koncu a insert w konkretnym miejscu
heros.insert(3,nowy_heros[0])
print(heros)
heros[1:3] = ["doctor strange"]

print(heros)
heros.sort()
print(heros)
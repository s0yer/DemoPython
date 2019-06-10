lista = [1,2,3,4,5]
lista.extend([6,7,8,9])
del(lista[0])
print(lista)

d = {'nome': 'Jadson'}
print(d.items())

for k, v in d.items():
    print(k, v)

del(d['nome'])
print(d)

t = (1,1,2,3,5,8,13,21)
print(t.index(1))
print(t)

s ={'Jadson', 'Keina', 'Katy'}
print(s)
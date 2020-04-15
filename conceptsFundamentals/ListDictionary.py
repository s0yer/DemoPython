
def listDictionary():

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
    print(t.index(5))
    print(t[4])
    print(t[t.index(5)])

    def veficicaIndice():
        if t[4] == t[t.index(5)]:
            return True
        else:
            return False
    print(veficicaIndice())

    print(t)

    s ={'Jadson', 'Keina', 'Katy'}
    print(s)
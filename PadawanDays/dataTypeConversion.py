# python 3.7

def dtConversion():
    dtConv_list = ['dtConversion()']
    i = 21.13853211

    inteiro = int(i)
    flutuante = float(i)
    corda = str(i)
    dtConv_list.append([[inteiro,flutuante,corda],[type(inteiro), type(flutuante), type(corda)],[pow(i, 2)]])

    print(inteiro)
    print(type(inteiro))
    print(flutuante)
    print(type(flutuante))
    print(corda)
    print(type(corda))



    return dtConv_list
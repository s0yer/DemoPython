# tuple/dictionary

def ArgumentosDicionario(*arg, **keywordArgs):
    list_args = ['ArgumentosDicionario()']
    print(keywordArgs)
    for k, argument in keywordArgs.items():
        print(k, argument)

    for elem in arg:
        print(elem)


        list_args.append([elem])

    return list_args

#dicionarios / Dictionaries

def callArgDic():

    ArgumentosDicionario(1, 1, 2, 3, 5, nome='Jadson', idade='27')

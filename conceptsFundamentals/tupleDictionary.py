# Python 3.7
# 010
# tuple/dictionary


def args_dictionary(*arg, **keywordArgs):
    list_args = ['args_dictionary()']
    print(keywordArgs)

    for k, argument in keywordArgs.items():
        print(k, argument)

    for elem in arg:
        print(elem)

        list_args.append([elem])

    return list_args


# Dictionary
def call_args_dict():
    args_dictionary(1, 1, 2, 3, 5, nome='Jadson', idade='27')

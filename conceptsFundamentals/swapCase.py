


def swap_case():
    s = "The future is Unpredictable"

    ns = ""
    list_swap_case = ['swap_case()']
    for elem in s:
        if elem.isupper() == True:
            ns+=(elem.lower())
        else:
            ns+=(elem.upper())
    list_swap_case.append(ns)
    print(ns)

    return list_swap_case
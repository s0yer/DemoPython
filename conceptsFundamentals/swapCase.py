

def swap_case(s):
    ns = ""
    for elem in s:
        if elem.isupper() == True:
            ns+=(elem.lower())
        else:
            ns+=(elem.upper())
    return ns
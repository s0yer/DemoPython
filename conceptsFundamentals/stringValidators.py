
"""
for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        any(eval("c." + test + "()") for c in s)

 eval should only ever be used with caution and
 there's usually a better solution. It's
 fragile (you may accidentally create invalid code)
 and can be dangerous (can offer ways for malicious
 code to be injected). It's also significantly slower,
 because the python code created by eval has to
 be recompiled on every iteration.
Eval is something to use for a quick hack but
it's not a good habit.

-------------------------------------------------

Other ways to solve:
t = type(s)
for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
    print any(method(c) for c in s)


-----------------------------------------------------------
any() is a core library function in Python.
It returns true if at least one value in the
sequence is true. It returns as soon as it
finds the first true value.
The any() function takes a sequence and returns
a single boolean.


"""
def stringValid():

    s = 'Future'
    string_list = ['stringValid()', s]

    # evaluates the parameters -> str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(method(c) for c in s))
        k = any(method(c) for c in s)
        string_list.append(k)

    return string_list

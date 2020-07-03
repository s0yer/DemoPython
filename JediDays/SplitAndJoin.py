# Python 3.7
# 218
from random import  randint

# change the spaces for especial characters
def split_and_join():
    list_log = ['split_and_join()']

    phrase = "To become the best you need to improve"
    list_log.append(phrase)

    # change space -> -
    s_split = phrase.split(" ")
    v_trace = "-".join(s_split)
    list_log.append(v_trace)

    # change - -> +
    t_split = v_trace.split("-")
    k_plus = "+".join(t_split)
    list_log.append(k_plus)

    # shuffle the source phrase
    size_phrase = len(s_split)
    bonus_list = []
    size_new_phrase = 0
    while size_new_phrase <= size_phrase:
        i = randint(0, size_phrase - 1)
        bonus_list.append(s_split[i])
        size_new_phrase = len(bonus_list)
    new_phrase = ' '.join(bonus_list)
    list_log.append(new_phrase)

    print('source: ' + phrase)
    print('swap -: ' + str(v_trace))
    print('swap *: ' + str(k_plus))
    print('bonus phrase: ' + new_phrase)

    return list_log


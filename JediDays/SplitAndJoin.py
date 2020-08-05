# Python 3.7
# 218

from random import randint
import aidfunctions

# change the spaces for especial characters
def split_and_join():

    phrase = "To become the best you need to improve"

    # change space -> -
    s_split = phrase.split(" ")
    v_trace = "-".join(s_split)

    # change - -> +
    t_split = v_trace.split("-")
    k_plus = "+".join(t_split)

    # shuffle the source phrase - on going
    source_split = phrase.split(" ")
    shuffle_list = []
    while len(source_split) != 0:
        elem = source_split.pop(randint(0,len(source_split)-1))
        shuffle_list.append(elem)
    new_shuffle_phrase = ' '.join(shuffle_list)

    # test if the loop is working and if the list is empty
    if len(new_shuffle_phrase) == 0:
        new_shuffle_phrase = 'on going'
    else:
        print('...')

    # create a new phrase source words based
    size_phrase = len(s_split)
    bonus_list = []
    size_new_phrase = 0
    while size_new_phrase <= size_phrase:
        i = randint(0, size_phrase - 1)
        bonus_list.append(s_split[i])
        size_new_phrase = len(bonus_list)
    new_phrase = ' '.join(bonus_list)

    print('source: ' + phrase)
    print('swap -: ' + str(v_trace))
    print('swap *: ' + str(k_plus))
    print('bonus phrase(shuffle): ' + new_shuffle_phrase)
    print('bonus phrase(disorder): ' + new_phrase)

    return aidfunctions.append_elements('split_and_join()', phrase, v_trace, k_plus, new_shuffle_phrase, new_phrase)



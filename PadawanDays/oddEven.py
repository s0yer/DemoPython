#odd and even

def oddEven():
    list_numbers = [-5,0,100,5,21,55,89,2,1,4,7,14,64,92,47,200,400]
    list_log = ['oddEven()']
    list_log.append(list_numbers)
    print(list_numbers)

    for el in list_numbers:
        if 0 <= el <= 100:
            if el % 2 == 0:
                if 2 <= el <= 5:
                    txt_ans = 'Weird (even)'
                    print(str(el) +' '+ txt_ans)
                elif 6 <= el <= 20:
                    txt_ans = 'Not Bad (even)'
                    print(str(el) +' '+ txt_ans)
                else:
                    txt_ans = 'ok (even)'
                    print(str(el) +' '+ txt_ans)

            else:
                txt_ans = '(odd)'
                print(str(el) +' '+txt_ans)
        else:
            txt_ans = 'imput a valid number! [0,100]'
            print(str(el) +' '+txt_ans)

        list_log.append(el)
        list_log.append(txt_ans)

    return list_log
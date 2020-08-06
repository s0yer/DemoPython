# Python 3.7
# 001

import aidfunctions

def writeArchive():

    #overwrite data
    arq = open('arq_demo.txt', mode='w') # sobrescreve / overwrite
    arq.write('salvando string...\n')
    arq.close()

    # open and add data / append
    arq = open('arq_demo.txt', mode='a')
    arq.write('adicionando conteudo ...\n')
    arq.close()

    # open and read
    arq = open('arq_demo.txt', mode='r')
    conteudo_arquivo=arq.read()
    arq.close()

    a = 'string'

    try:
        # uso de with
        arq = open('arq_demo.txt', mode='a')
        a = 'Testa se esta escrevendo! / try write test'
        arq.write(a + '\n')
        #entrada_usuario = input('Digite algo: ')
        arq.close()
    except IOError:
        a = 'arquivo nao encontrado / archive not found'
        print(a)
    except ValueError:
        a = 'Erro de valor / value error'
        print(a)
    except:
        a = 'Erro desconhecido / coringa / unknown errors'
        print(a)
    finally:
        b = 'Cleanup'
        print(b)

    print('Fim.')

    return aidfunctions.append_elements('writeArchive()', a, b)
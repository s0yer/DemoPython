

def writeArchive():

    arq = open('arq_demo.txt', mode='w') # sobrescreve / overwrite
    arq.write('salvando string...\n')
    arq.close()

    arq = open('arq_demo.txt', mode='a')
    arq.write('adicionando conteudo ...\n')
    arq.close()

    arq = open('arq_demo.txt', mode='r')
    conteudo_arquivo=arq.read()
    arq.close()

    try:
        # uso de with
        with open('arq_demo.txt', mode='w') as arq:

            arq.write('Testa se esta fechando !')
        #entrada_usuario = input('Digite algo: ')

    except IOError:
        print('arquivo nao encontrado')
    except ValueError:
        print('Erro de valor')
    except:
        print('Erro desconhecido / coringa')
    finally:
        print('Cleanup')

    print('Fim.')

writeArchive()
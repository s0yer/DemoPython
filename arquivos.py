arq = open('arq_demo.txt', mode='w') # sobrescreve
arq.write('salvando string...')
arq.close()

arq = open('arq_demo.txt', mode='a')
arq.write('adicionando conteudo ...')
arq.close()

arq = open('arq_demo.txt', mode='r')
conteudo_arquivo=arq.read()
arq.close()

print(conteudo_arquivo)


# Python 3.7
# UNICAMP - P_IA012A_2020S2 - Segurança em Comunicação de Dados
# Este e um projeto Academico ex.9


from random import randint

text_p = 'jadsonmarlieredeoliveira'
k1 = 0

if k1 < 4:
    k1 = 4
else:
    print('ok')

size_p = len(text_p)

k2 = []
for elem in range(21, 34):
    k2.append(randint(1, size_p/k1))

print('Texto em claro: ')
print(text_p)
print('Chaves: ')
print('k1 = {}'.format(k1))
print('k2 = {}'.format(k2))



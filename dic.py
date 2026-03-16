'''#Dicionário
aluno = {
    'nome': 'Lucas',
    'matricula': 123456,
    'turma': '1E',
    'notas': [7.5, 8, 5]
}

aluno['nome'] = 'tiago'
aluno ['senha'] = 123456

print (aluno)
print (aluno['nome'])
print ("notas:", aluno['notas'])
'''




'''
#Exercício_11: 
contato = {
    'nome': "Bela",
    'telefone': "31999997777",
    'email': "isabela@gmail.com",
    'cidade': "Rio Pomba"
}

for chave, valor in contato.items():
    print(f'{chave}: {valor}')

contato['instagram'] = 'bela@'
print (contato['instagram'])

del contato['telefone']
removido = contato.pop('telefone')
print (contato['telefone'])

if 'email' in contato:
    print('Chave existe!')
''' 

'''#Exercício_12:
frase = 'o rato roeu a roupa do rei de roma'
palavras = frase.split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

for chave, valor in contagem.items():
    print(f'{chave}: {valor}')
'''

'''#Exercício_13:
turma = {
    "bela": [8.5, 10.0, 9.0],
    "milena": [6.0, 5.5, 7.0],
    "tiago": [9.5, 10.0, 9.0],
    "fulano": [7.0, 8.0, 7.5]
}
for aluno, notas in turma.items():
    media = sum(notas) / len(notas)
    
    if media >= 6.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(aluno + " – Média: " + str(media) + " – Situação: " + situacao)
'''

#Exercício_14:
info1 = {'nome': 'Notebook', 'preco': 3500.00}
info2 = {'marca': 'TechBrand', 'estoque': 15}

total = {**info1, **info2}
print (total)

info1['preco'] = 3200.00
total = {**info1, **info2}
print (total)

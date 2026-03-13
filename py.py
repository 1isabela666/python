'''#Ex_1:
notas = ['7.5', '8.0', '6.0', '9.5', '5.0']

notas.append ('8.5')
print (notas)

notas[4] = '6.5'
print (notas)

notas.sort(reverse=True)
print (notas)
maior = max(notas)

menor = min(notas)

print(f"Maior: {maior}, Menor: {menor}")
'''

'''#Ex_2:
nomes = ["Bela", "Milena", "Tiago", "Marreta", "Bernardo"]
print (nomes)

for i, nomes in enumerate(nomes):
    print(f'{i}: {nomes}')
'''

'''#Ex_3:
numeros = [3, 17, 8, 42, 5, 100, 23, 66, 11, 99]
for num in numeros:
    if num % 2 == 0:
        print(num)

num2 = [21, 25, 30, 57, 86, 149]
total = sum(num2)
print (total)
'''

'''#Ex_4: 
numeros = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[:4])
print(numeros[8:])
print(numeros[::2])
'''

'''#Ex_5:
turma = [["Bela", 9.0], ["Milena", 9.5], ["Tiago", 9.8], ["Bernardo", 7.0]]
for item in turma:
    print(item)
'''

#Ex_7:
aluno = (Bela, terceiro, 10, "Python")

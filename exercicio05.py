
lista = []
for _ in range(5):
    valor = int(input('Valor --> '))
    lista.append(valor)
    
# invertendo os valores do vetor usando apenas lógica de programação
j = len(lista) - 1
for i in range(len(lista) // 2):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
    j -= 1
    
print(lista)

# invertendo os valores usando o conceito de tupla
j = len(lista) - 1
for i in range(len(lista) // 2):
    lista[i], lista[j] = lista[j], lista[i]
    j -= 1
    
print(lista)

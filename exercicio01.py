lista = []
maior = float('-inf')
menor = float('inf')

# entrada de dados
for i in range(5):
    lista.append(int(input('Digite o valor --> ')))
    if lista[i] > maior:
        maior = lista[i]
        
    if lista[i] < menor:
        menor = lista[i]
        
print(f'maior = {maior}')
print(f'menor = {menor}')
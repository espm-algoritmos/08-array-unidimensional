lista = []
par = 0

for i in range(5):
    lista.append(int(input('Digite o valor --> ')))
    if lista[i] % 2 == 0:
        par += 1
        
print(f'total de pares --> {par}')
print(f'total de ímpares --> {len(lista) - par}')
print(f'porcentagem de pares --> {par / len(lista) * 100:.2f}%')
print(f'porcentagem de ímpares --> {100 - par / len(lista) * 100:.2f}%')
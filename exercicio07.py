
binario = []
valor = int(input('Valor na base decimal --> '))
if valor < 0:
    print('valor deve ser positivo')
else:
    while valor > 0:
        binario.append(valor % 2)
        valor = valor // 2
    
    for i in range(len(binario)-1, -1, -1):
        print(f'{binario[i]}', end='')
        
    
lista = []

for i in range(5):
    valor = int(input("informe um valor: "))
    lista.append(valor)
    
print(lista)

# impressão de elemento a elemento
for i in range(len(lista)):
    print(lista[i], end='  ')
    
# impressão dos elementos do final para o início
print()
for i in range(len(lista)-1, -1, -1):
    print(lista[i], end='  ')
#

linha = int(input('digite o número de linhas: '))
coluna = int(input('digite o número de colunas: '))

matriz = []

for i in range(linha):
    aux = []

    for j in range(coluna): 
       val= int(input(f'digite um valor de [{i}][{j}]: '))
       aux.append(val)
    matriz.append(aux)  

for linha in matriz:
    print(linha)




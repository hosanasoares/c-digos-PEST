#refazer o programa anterior usando funções

def retorna_maior(l : list):
    maior_numero = l[0]

    for item in l:
        if item > maior_numero:
            maior_numero = item
    
    return maior_numero



lista = [1, 344, -15, 1989, 2007, 23.5, 12, 25, 67.3]
print(retorna_maior(lista))
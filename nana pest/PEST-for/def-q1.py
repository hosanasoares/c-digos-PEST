def area(largura : float, comprimento : float):
    mult = (largura * comprimento)

    print('a área do terreno', largura, 'x', comprimento,'é:', mult)

larg = float(input('digite a largura do terreno:'))
compr = float(input('digite o comprimento do terreno: '))

area(larg, compr)
def converter(moeda : float, dolar : bool =True):
    if dolar:

        tx =  5.30
        convert = moeda / tx
        return convert
    
    else:
        return moeda
    



moeda = float(input('digite o valor em moeda:'))
res = converter(moeda)
print(res)
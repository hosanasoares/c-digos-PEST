def moeda(real:float,dolar:bool='True'):
    taxa = 5.30
    if dolar:
        return real/dolar
    else:
        return real

print(f'U$ {moeda(100)}')
print(f'R$ {moeda(100, False)}')
    
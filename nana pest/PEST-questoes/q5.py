def conversor_moedas(real : float, taxa : float):
    dolar = real / taxa

    return dolar



real = float(input('digite o valor em reais: '))
taxa = float(input('digite a taxa: '))

while real < 0:
    real = float(input('digite o valor em reais: '))

while taxa < 0:
    taxa = float(input('digite a taxa: '))

res = conversor_moedas(real,taxa)

print('o valor do real em dólar é:', res)
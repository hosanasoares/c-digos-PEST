def escreva(palavra : str):
    tam = len(str(palavra))
    print('-'*tam)
    print(palavra)
    print('-'*tam)

plv = str(input('escreva uma palavra/frase: '))
escreva(plv)
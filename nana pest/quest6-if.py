num = int(input('digite um número com cinco '))

unidade = num % 10
dezena  = (num-unidade/10) % 10
dez_mi =num//10000
milhar  = (num//1000) % 10 
centena = (num-milhar-dez_mi)//100

if (unidade == dezena or unidade == centena or unidade == milhar) or (dezena == centena or dezena == milhar or dezena == dez_mi) or (centena == milhar or centena == dez_mi)or (milhar == dez_mi):
    print('há um número que se repete.')

else:
    print('todos os números são diferentes.')
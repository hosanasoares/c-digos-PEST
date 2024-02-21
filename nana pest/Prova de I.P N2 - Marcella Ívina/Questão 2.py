# Verificação de CPF
cpf = str(input('Insira seu CPF: '))

while len(str(cpf)) != 11:
    print(f'{cpf} este CPF é inválido, digite novamente.')
    cpf = int(input('Insira seu CPF novamente: '))
print('Seu CPF é válido, guardamos ele no nosso sistema.')
print("Digite o que deseja fazer: [1] adicionar \n[2] Remover \n[3]Ver \n[4]Sair')")
lista = []
while True:
    op = str(input('digite uma opção: '))

    if op == '1':
        ad = str(input('digite um paciente: ')).lower()

        if ad in lista:
            print('paciente já está na lista.')

        else:
         print('paciente adicionado')
         lista.append(ad)

    elif op == '2':
      copia = lista[:]  

      if lista == []:
        print('paciente não existe!')
     
      else:
            del copia[0]
            print('paciente removido')

    elif op == '3':
        print(copia)

    elif op == '4':
       break

    else:
       print('não existe')

print(copia)
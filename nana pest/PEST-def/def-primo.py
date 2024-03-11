def primo(num:int):
    cont = 0
   
    for h in range(1,num+1):
        if num % h == 0:
            count+=1
    
    if count == 2:

        return True
    return False



count = 0
hosana = 0
while True:
    n = int(input('digite um número.'))

    if primo(n):
        print(n, 'é primo')
        count +=1
    if n == 0:
        break

print()

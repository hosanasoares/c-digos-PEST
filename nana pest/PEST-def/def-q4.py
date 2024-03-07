def primo(num : int, primo : bool = True):
        if primo:
            count = 0

        for i in range(1,num+1):
              if num % i == 0:
                    count += 1
        if count == 2:
              return True
        
        else:
              return False
        

n = int(input('digite um número: '))

res = primo(n)
print(res)
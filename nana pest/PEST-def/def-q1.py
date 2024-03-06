def calculadora(num1 : float, num2 : float, op : str):
    if op == 'soma' or op == 's':
        x = num1 + num2
      

    elif op == 'subtração' or op == 'sub':
        x = num1 - num2
        

    
    elif op == 'multi' or op == 'multiplicação':
        x = num1 * num2
        
    return x

n = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))
op = str(input('digite a operação que deseja realizar: ')).lower()
res = calculadora(n,n2,op)  
print(res) 
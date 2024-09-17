n1 = int(input('Digite um numero inicial: '))
n2 = int(input('Digite um numero final: '))

if n1 <= n2:
         for n in range(n1, n2 + 1):
              print(n)
else:
    print('O numero inicial deve ser menor ou igual ao final')
    
    

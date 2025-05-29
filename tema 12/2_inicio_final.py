numeroInicial = int(input('Digite um numero inicial: '))
numeroFinal = int(input('Digite um numero final: '))

if numeroInicial <= numeroFinal:
         for n in range(numeroInicial, numeroFinal + 1):
              print(n)
else:
    print('O numero inicial deve ser menor ou igual ao final')

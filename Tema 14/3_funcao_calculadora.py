#Função de soma
def soma(a, b):
    return a + b
#Função de subtração
def subtracao(a, b):
    return a - b
#Função de multiplicação
def multiplicacao(a, b):
    return a * b
#Função de divisão
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida"
# Digitação de numeros inteiros
num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
# Fazendo a soma e mostrando o resultado
print("Soma:", soma(num1, num2))
print("Subtração:", subtracao(num1, num2))
print("Multiplicação:", multiplicacao(num1, num2))
print("Divisão:", divisao(num1, num2))

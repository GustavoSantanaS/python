# função que ira multiplicar a idade do usuario por um ano
# E mostrara quantos dias aproximadamente ja viveu
def dias_de_vida(nome, idade):
    dias = idade * 365
    return nome + ", você já viveu aproximadamente " + str(dias) + " dias."

# Entrada de dados do usuario e print na tela da função
nome_usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite sua idade: "))
print(dias_de_vida(nome_usuario, idade_usuario))

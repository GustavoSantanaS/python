import cimc       #importa o modulo que tem as funcoes pra calcular e classifica
                  #orecisa do arquivo cimc
#solicita ao usuario pesso em quilogramas e altura em metros
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))
#calcula o imc e classifica
imc = cimc.calcular_imc(peso, altura)
classificacao = cimc.classificar_imc(imc)
#exibe o imc e a classificacao
print("Seu IMC é:", imc)
print("Classificação:", classificacao)

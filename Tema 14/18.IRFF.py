#entradaa de dados do usuario que colocara o quanto de dinheiro ganha
salario_bruto = float(input("Digite o valor do salário bruto: R$ "))

# Cálculo do INSS
if salario_bruto <= 1693.72:
    inss = salario_bruto * 0.08
elif salario_bruto <= 2822.90:
    inss = salario_bruto * 0.09
elif salario_bruto <= 5645.80:
    inss = salario_bruto * 0.11
else:
    inss = 5645.80 * 0.11

# Cálculo do salário base
salario_base = salario_bruto - inss

# Cálculos do IRRF
if salario_base <= 1903.98:
    irrf = 0
elif salario_base <= 2826.65:
    irrf = salario_base * 0.075 - 142.80
elif salario_base <= 3751.05:
    irrf = salario_base * 0.15 - 354.80
elif salario_base <= 4664.68:
    irrf = salario_base * 0.225 - 636.13
else:
    irrf = salario_base * 0.275 - 869.36

# Cálculo do salário líquido
salario_liquido = salario_base - irrf
# Mostra os resultados
print("Salário Bruto: R$", salario_bruto)
print("Desconto INSS: R$", inss)
print("Desconto IRRF: R$", irrf)
print("Salário Líquido: R$", salario_liquido)

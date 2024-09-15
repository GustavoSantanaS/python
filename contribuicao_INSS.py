def calcular_inss(salario_bruto):
    if salario_bruto <= 1693.72:
        inss = salario_bruto * 0.08
    elif salario_bruto <= 2822.90:
        inss = salario_bruto * 0.09
    elif salario_bruto <= 5645.80:
        inss = salario_bruto * 0.11
    else:
        inss = 5645.80 * 0.11

    return inss

def calcular_salario_liquido(salario_bruto):
    inss = calcular_inss(salario_bruto)
    salario_liquido = salario_bruto - inss
    return salario_liquido, inss

salario_bruto = float(input("Digite o valor do salário: R$ "))

salario_liquido, inss = calcular_salario_liquido(salario_bruto)

print("Salário: R$", salario_bruto)
print("Contribuição ao INSS: R$", inss)
print("Salário Líquido: R$", salario_liquido)

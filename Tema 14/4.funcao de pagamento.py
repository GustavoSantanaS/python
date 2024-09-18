# função que ira multiplicar o valor a receber por hora trabalhada
def pagamento(horas_trabalhadas, valor_por_hora):
    valor_total = horas_trabalhadas * valor_por_hora
    return valor_total

# entrada de dados pelo usuario
horas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora: "))
total_a_pagar = pagamento(horas, valor_hora)
# ira mostrar os resultados
print("O valor a ser pago é: R$", total_a_pagar)

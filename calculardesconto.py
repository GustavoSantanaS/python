preco_original = float(input("Digite o preço original do produto: R$ "))
porcentagem_desconto = float(input("Digite a porcentagem do desconto(%): "))

valor_desconto = preco_original * (porcentagem_desconto / 100)

novo_preco = preco_original - valor_desconto

print("Preço original: R$", preco_original)
print("Desconto: R$", valor_desconto)
print("Preço com desconto: R$", novo_preco)
 

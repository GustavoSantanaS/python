def data_por_extenso(data):
    # Verifica se a data está no formato correto
    if len(data) != 10 or data[2] != '/' or data[5] != '/':
        return "Data inválida"
    
    dia_str, mes_str, ano = data[:2], data[3:5], data[6:]
    
    # Verifica se os valores são numeros inteiros
    try:
        dia = int(dia_str)
        mes = int(mes_str)
    except ValueError:
        return "Data inválida"
    
    # Lista dos meses 
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    
    # Verifica se o mês e o dia são válidos
    if mes < 1 or mes > 12 or dia < 1 or dia > 31 or (mes == 2 and dia > 29) or (mes in [4, 6, 9, 11] and dia > 30):
        return "Data inválida"
    
    # Deixa a data no formato desejado dia meses e ano
    return str(dia) + ' de ' + meses[mes - 1] + ' de ' + ano

# formas de uso(ira aparecer) se estiver certo ou errado
print(data_por_extenso('18/09/2024'))  # Saida de dados: 18 de setembro de 2024
print(data_por_extenso('31/02/2024'))  # Saida de dados: Data inválida

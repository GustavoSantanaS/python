from funk import media_aluno
#para funcionar o exemplo a cima e preciso ter o arquivo com o nome funk na mesma pasta
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a nota do trabalho: '))

print('')
media_final = media_aluno(n1,n2,n3)
print('A sua media final do aluno é: ', media_final)

def cifra_de_cesar(mensagem, chave):
    mensagem_criptografada = ""
    for caractere in mensagem:
        if caractere.isalpha():
            deslocamento = 65 if caractere.isupper() else 97
            mensagem_criptografada += chr((ord(caractere) - deslocamento + chave) % 26 + deslocamento)
        else:
            mensagem_criptografada += caractere
    return mensagem_criptografada

mensagem = input("Digite a mensagem para criptografar: ")
chave = int(input("Digite o valor da chave (deslocamento): "))
mensagem_criptografada = cifra_de_cesar(mensagem, chave)

print("Mensagem criptografada:", mensagem_criptografada)

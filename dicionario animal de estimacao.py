animal_de_estimacao = {
    "nome": "Rex",
    "tipo": "Cachorro",
    "idade": 5,
    "raça": "Labrador",
    "peso": 30.5,
    "vacinas": ["Raiva", "Parvovirose", "Cinomose"]
                      }

print("Informações do Animal de Estimação:")
print("Nome: " + animal_de_estimacao['nome'])
print("Tipo: " + animal_de_estimacao['tipo'])
print("Idade: " + str(animal_de_estimacao['idade']) + " anos")
print("Raça: " + animal_de_estimacao['raça'])
print("Peso: " + str(animal_de_estimacao['peso']) + " kg")
print("Vacinas: " + ", ".join(animal_de_estimacao["vacinas"]))

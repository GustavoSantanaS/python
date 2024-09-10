#digitação pelo codigo string  
nota_str = input("digite uma nota: ")
#transformando a var em real
nota_float = float (nota_str)

if nota_float >= 6:
    print("Parabens, voce foi aprovado")
elif nota_float >= 4 and nota_float < 5.9:
    print("voce esta de recuperacao")
    
else:
    print ("Não foi aprovado desta vez")

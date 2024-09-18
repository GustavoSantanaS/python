import triangulo #precisa do arquivo triangulo na mesma pasta

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

area = triangulo.calcular_area(base, altura)
print("A área do triângulo é:", area)

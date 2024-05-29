def calcular_area_quadrado(lado):
    return lado ** 2

lado = float(input("Por favor, insira o comprimento do lado do quadrado: "))

area = calcular_area_quadrado(lado)

dobro_area = 2 * area

print(f"A área do quadrado com lado {lado} é: {area:.2f}")
print(f"O dobro da área do quadrado é: {dobro_area:.2f}")

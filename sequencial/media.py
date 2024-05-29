def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

notas = []
for i in range(4):
    nota = float(input(f"Por favor, insira a nota do {i+1}º bimestre: "))
    notas.append(nota)

media = calcular_media(notas)

print(f"A média das notas bimestrais é: {media:.2f}")

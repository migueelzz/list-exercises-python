numero1 = float(input("Por favor, insira o primeiro número: "))
numero2 = float(input("Por favor, insira o segundo número: "))

if numero1 > numero2:
    maior = numero1
elif numero2 > numero1:
    maior = numero2
else:
    maior = None

if maior is not None:
    print(f"O maior número entre {numero1} e {numero2} é: {maior}")
else:
    print("Os dois números são iguais.")

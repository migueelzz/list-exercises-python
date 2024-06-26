numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print("Números no intervalo:", end=" ")
for numero in range(numero1 + 1, numero2):
    print(numero, end=" ")

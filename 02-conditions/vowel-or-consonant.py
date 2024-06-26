letra = input("Por favor, insira uma letra: ").lower()

if letra in 'aeiou':
    print(f"A letra '{letra}' é uma vogal.")
elif letra.isalpha() and len(letra) == 1:
    print(f"A letra '{letra}' é uma consoante.")
else:
    print("Entrada inválida. Por favor, insira uma única letra.")

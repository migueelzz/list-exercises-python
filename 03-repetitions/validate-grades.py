while True:
    nota = float(input("Por favor, insira uma nota entre zero e dez: "))
    
    if 0 <= nota <= 10:
        print(f"Você inseriu a nota {nota}.")
        break
    else:
        print("Valor inválido. Por favor, insira uma nota entre zero e dez.")

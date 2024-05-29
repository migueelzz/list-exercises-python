while True:
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    if senha != usuario:
        print("Cadastro realizado com sucesso!")
        break
    else:
        print("Erro: A senha não pode ser igual ao nome de usuário. Por favor, tente novamente.")

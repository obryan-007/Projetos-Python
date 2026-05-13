
#Lista de logins:
usuarios = [
    {"usuário": "Bryan", "senha": "121510"}
    ]

try:
    while True:
        #ÁREA DE LOGIN:
        print("\n\n---ÁREA DE LOGIN---")
        print("1. Entrar na conta")
        print("2. Criar uma nova conta")
        print("3. Lista de Usuários.")
        print("4. Excluir conta")
        print("5. Sair\n")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nEntrar na conta")
            usuario_digitado = input("Digite o usuário: ") 
            senha_digitada = input("Digite a senha: ")
            login_correto = False
            for user in usuarios:
                if usuario_digitado == user["usuário"] and senha_digitada == user["senha"]:
                    login_correto = True
                    break
            if login_correto:
                print("\nLogin bem-sucedido.")
            else:
                print("Login ou senha incorretos ou usuário inexistente, tente novamente!")
                continue
                    
         
        elif opcao == '2':
            print("\nCrie uma nova conta")
            usuario_novo = input("Digite o nome do usuário: ")
            senha_nova = input("Digite a senha que deseja: ")
            login_igual = False
            for user in usuarios:
                if usuario_novo == user['usuário']:
                    login_igual = True
            if login_igual:
                print("Já existe uma conta com este usuário.")
            else:
                usuarios.append({'usuário': usuario_novo, "senha": senha_nova})
                print(f"Conta {usuario_novo} criada.")


        elif opcao == '3':
            print('Lista de usuários:')
            for numero, user in enumerate(usuarios, start=1):
                print(numero, '-' , user['usuário'])
                
    

        elif opcao == "4":
            for numero, user in enumerate(usuarios, start=1):
                print(numero, "-", user["usuário"])
            print('Qual usuário da lista deseja remover?')
            exclusao = int(input('Escolha o número para exclusão: '))
            indice = int(exclusao) - 1
            usuário_removido = usuarios.pop(indice)
            print(f'Você excluiu {usuário_removido["usuário"]}')

        elif opcao == "5":
            print("Encerrando menu...")
            break

        else:
            print("Opção inválida, tente novamente.")
            continue

except(KeyboardInterrupt, KeyError, EOFError):
    print("\nSistema encerrado pelo usuário.")
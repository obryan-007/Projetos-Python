nomes = ["Bryan", "Raissa", "Vinicius", "Gustavo"]


try:
     while True:
         print("\n---Entrada da Festa, selecione uma opção abaixo---")
         print("\n1. Entrar na festa")
         print("2. Verificar meu nome na lista")
         print("3. Fechar programa")
         opcao = input("Escolha uma opção acima: ")

         if opcao == "1":
             nome = input("\nEpa, epa. Qual é o seu nome?\n")
             if nome not in nomes:
                 print("\nSinto muito, seu nome não esta na lista")
                 escolha = input("Gostaria de tentar outro nome? (S/N): ").lower()
                 if escolha == "n":
                     print("\nCerto, tchau.")
                     break
                 else:
                     continue
             else:
                 print('Seja bem-vindo a festa!!!')
                 break
             
         elif opcao == "2":
             print("\n---Lista dos convidados---")
             for numero, nome in enumerate(nomes, start= 1):
                print(f'{numero} - {nome}')


         elif opcao == "3":
             print("---Encerrando programa---")
             break
         
         else:
             print("Opção inválida, tente novamente\n")
             
            
except (KeyboardInterrupt, KeyError, EOFError):
     print("\n---Programa encerrado pelo usuário---")
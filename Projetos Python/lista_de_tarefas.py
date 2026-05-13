lista = []

try:
    while True:

        print("\n---Lista de tarefas---")
        print("1. Adicionar item a lista")
        print("2. Ver lista completa")
        print("3. Excluir um item da lista")
        print("4. Sair do programa")
        opcao = input("\nEscolha uma das opções acima: ")

        if opcao ==  "1":
            print("\nVocê escolheu a opção 'Adicionar item' ")
            item = input("Escreva um item que deseja adicionar: ")
            lista.append(item)
            print(f"Você adicionou '{item}'.")


        elif opcao == "2":
            if not lista:
             print("\nSua lista está vazia, adicione algum item!")

            else:
              print("\nLista completa:")
              for ordem, item in enumerate(lista, start = 1):
                 print(f"{ordem} - {item}")

        elif opcao == "3":
            print("\nVocê escolheu a opção 'Excluir um item' ")
            if not lista:
               print("Não tem nenhum item na lista para excluir.")
            else:
               numero = int(input("Qual item da lista você deseja remover: "))
               indice = int(numero) - 1
               item_removido = lista.pop(indice)
               print(f'"{item_removido}" foi removido.')

        elif opcao == "4":
            print("\n---Encerrando programa.---")
            break
            
        else:
            print("\nSelecione alguma opção acima!")

except (KeyboardInterrupt, KeyError, EOFError):
    print('Sistema encerrado pelo usuário...')
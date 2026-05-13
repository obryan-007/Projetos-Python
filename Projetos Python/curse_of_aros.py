#Contador de Shards

#Calcula quantos shards você terá e qual o valor de acordo com oque o usuário digitar
def calcular_lollipop():
    try:
        print("\n-------------------------------------------")
        shards = int(input("Quantas Lollipop você tem?\nR: "))
        valor = int(input("Quanto custa cada Lollipop?\nR: "))
        valor_final = shards * valor
        total_shards = shards * 5
        print(f'Você terá um total de "{total_shards:,}" Shards'.replace(",", "."))
        print(f'O valor final ficará {valor_final:,} de gold'.replace(",", "."))
    except ValueError:
        print("Somente números!")

#Calcula quantos lollipop o usuário terá
def calcular_shards():
    try:
        print("\n-------------------------------------------")
        lollipop = int(input("Quantos Shards você tem?\nR: "))
        total_lolli = lollipop / 5
        print(f'Você terá um total de "{total_lolli:,.0f}" Lollipops'.replace(",", "."))
    except ValueError:
        print("Somente número!")

#Menu de opção
def menu():
    while True:
        try:
            print("\n-------------------------------------------")
            print("Calculadora de Shards")
            print("1 - Calcular quantos Shards você terá")
            print("2 - Calcular quantos Lollipop você terá")
            print("3 - Sair")
            print("-------------------------------------------")
            opcao = int(input("Seleciona uma opção: "))
        except ValueError:
            print("Somente números!")
            continue

        match opcao:
            case 1:
                calcular_lollipop()
            case 2:
                calcular_shards()
            case 3:
                print("Encerrando...")
                break
            case _:
                print("Escolha alguma opção acima")
                continue

#Chama a função
menu()
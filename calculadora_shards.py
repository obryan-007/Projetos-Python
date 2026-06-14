# * Sugestões *
#Criar uma definição para o valor da lollipop.
#Histórico dos valores digitados pelo usuário


#Contador de Shards

#Calcula quantos shards você terá e qual o valor de acordo com oque o usuário digitar
def calcular_lollipop():
    try:
        print("\n-------------------------------------------")
        lolli = int(input("Quantas Lollipop você tem?\nR: "))
        valor = int(input("Quanto custa cada Lollipop?\nR: "))
        if lolli and valor >= 0:
            valor_final = lolli * valor
            total_shards = lolli * 5
            print(f'Você terá um total de "{total_shards:,}" Shards'.replace(",", "."))
            print(f'O valor final ficará {valor_final:,} de gold'.replace(",", "."))
        else:
            print("Digite um número válido!")
    except ValueError:
        print("Somente números!")

#Calcula quantos lollipop o usuário terá
def calcular_shards():
    try:
        print("\n-------------------------------------------")
        shard = int(input("Quantos Shards você tem?\nR: "))
        if shard >= 0:
            total_lolli = shard / 5
            print(f'Você terá um total de "{total_lolli:,.0f}" Lollipops'.replace(",", "."))
        else:
            print("Digite um número válido")
    except ValueError:
        print("Somente números!")

#Converte todo o seu gold em lollipop e shards, de acordo com o valor do lollipop que o usuário digitar
def converter_gold():
    try:
        gold = int(input("Quanto de Gold você quer converter? \nR: "))
        valor_lolli = int(input("Quanto custa cada Lollipop?\nR: "))
        if gold and valor_lolli >= 0:
            conversão = gold // valor_lolli
            print(f'Você poderá comprar "{conversão:,.0f}" Lollipops e terá {conversão*5:,.0f} Shards'.replace(",", "."))
        else:
            print("Digite um número válido!")
    except ValueError:  
        print("Somente números!")

#Menu de opção
def menu():
    while True:
        try:
            print("\n-------------------------------------------")
            print("Calculadora de Shards")
            print("1 - Converter Lollipop em Shard")
            print("2 - Converter Shard em Lollipop")
            print("3 - Converter Gold em Lollipop/Shard")
            print("4 - Sair")
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
                converter_gold()
            case 4:
                print("Encerrando...")
                break
            case _:
                print("Escolha alguma opção acima")
                continue

#Chama a função
menu()
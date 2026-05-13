#A váriavel 'acerto' tem que começar com 0 e estar fora do while true
acerto = 0

while True:
    #Início do Quiz
    print("\n--- Quiz! Você consegue acertar? ---")
    print('Você respondaram 10 perguntas e será somado o quanto você acertou!')
    pergunta_1 =  input('\n1°- Qual a capital do brasil? \na) São paulo \nb) Brasília \nc) Rio de Janeiro \nd) Distrito Federal \nResposta(somente alternativa): ')

    #Primeira pergunta
    if pergunta_1 == "b":
        #Se usuário acerta a pergunta, o computador irá guardar o valor 'acerto += 1' e acrescentará 1 ponto
        acerto += 1
        print("Acertou!")
    else:
        #Caso contrário, não contabiliza
        print('Errou!')

    pergunta_2 = input('\n2°- Qual o animal terrestre mais rápido do planeta? \na) Leão \nb) Leopardo \nc) Urso \nd) Tigre \nResposta: ')

    if pergunta_2 == "b":
        acerto += 1
        print('Acertou!')
    else:
        print('Errou!')
    
    pergunta_3 = input('\n3°- Qual é a distância entre a Terra e a Lua \na) 330 mil KM \nb) 500 mil KM \nc) 375 mil KM \nd) 380 mil KM \nResposta: ')

    if pergunta_3 == "d":
        acerto += 1
        print('Acertou!')
    else:
        print('Errou!')

    pergunta_4 = input('\n4°- Quem traiu Jesus Cristo? \na) Simão \nb) Tomé \nc) Judas Escariotes \nd) André \nResposta: ')

    if pergunta_4 == "c":
        acerto += 1
        print('Acertou!')
    else:
        print('Errou!')

    pergunta_5 = input('\n5°- Qual casa do conto "Os Três Porquinhos" não foi derrubada \na) Palha \nb) Madeira \nc) Pedra \nd) Tijolo \nResposta: ')

    if pergunta_5 == "d":
        acerto += 1
        print('Acertou!')
    else:
        print('Errou!')

    #Resultado final
    if acerto <= 2:
        print(f'\nEh, você acertou {acerto} perguntas. Melhorar na próxima!')
    elif acerto >= 3:
        print(f'\nOK, você acertou {acerto} perguntas. Bom, porém pode melhorar.')
    elif acerto == 5:
        print(f"\nParábens! Voce acertou {acerto} perguntas. Acertou tudo, parábens.")

    #Conclusão, após as perguntas acabarem o computador irá perguntar ao usuário se deseja tentar novamente
    continuar = input('Deseja tentar novamente? Sim ou Não? \nResposta: ').lower()

    #Se o usuário digitar: sim, sistema continua.
    if continuar == 'sim':
        #A varíavel 'acerto' volta a 0, se não iria continuar contabilizando das perguntas de antes
        acerto = 0
        continue
    #Caso contrário, sistema fehca com o 'break'
    else:
        print('\nFim de jogo!')
        break

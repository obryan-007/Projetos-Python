
import random

while True:
 print("\n---MENU DE JOGOS---")
 print("1. Pedra, papel ou tesoura?")
 print("2. Adivinhe o número!")
 print("3. Sair")
 escolha = input("\nEscolha uma das opções acima: ")
 print("\n------------------------------------------------------------")

 if escolha == "1":
    while True:
     opcoes = ["pedra", "papel", "tesoura"]
     escolha_cpu = random.choice(opcoes)
     print("\n---PEDRA, PAPEL OU TESOURA?---")
     escolha_jogador = input("\n---Escolha pedra, papel ou tesoura: ").lower()
     if escolha_jogador not in opcoes:
        print("---Opção inválida, escolha novamente---")
     else:
        print(f"---Você escolheu {escolha_jogador}, e a CPU escolheu {escolha_cpu}!---")
        break
        
    if escolha_jogador == escolha_cpu:
       print("---Vocês empataram!---")

    elif escolha_jogador == "pedra" and escolha_cpu == "tesoura":
      print("\n---Você venceu!---")
 
    elif escolha_jogador == "papel" and escolha_cpu == "pedra":
      print("\n---Você venceu!---")

    elif escolha_jogador == "tesoura" and escolha_cpu == "papel":
      print("\n---Você venceu!---")

    else:
       print("\n---Ah não, Você perdeu!---")
    print("\n-------------------------------------------------------")

 
 elif escolha == "2":
    secreto = random.randint(1, 10)
    tentativa = 0
    while True:
     try:
        
        print("\n----JOGO DA ADIVINHAÇÃO---")
        palpite = int(input("Escolha um número inteiro: "))
        tentativa += 1
     except ValueError:
        print("Por favor, use somente números inteiros!\n")
        continue
 
     if palpite == secreto:
         print("\n---Parabéns! Você acertou!---")
         print(f"---Você acertou em um total de {tentativa} tentativas---\n")
         break
    
     if palpite > 10:
        print("O número tem que ser menor que 10!")
        continue
     
     elif palpite < secreto:
        print("O número é maior!\n")
        continue

     elif palpite > secreto:
        print("O número é menor!\n")
        continue
    
 elif escolha == "3":
    print("\n---Encerrando programa!---")
    break
 
 else:
    print("\nOpção invalida! Tente novamente.")
    print("\n-------------------------------------------------------")    
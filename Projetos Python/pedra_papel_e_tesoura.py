import random

opcoes = ["pedra", "papel", "tesoura"]
escolha_cpu = random.choice(opcoes)

while True:
    print("\n\n---PEDRA, PAPEL OU TESOURA?---")
    escolha_jogador = input("\n---Escolha pedra, papel ou tesoura: ").lower()
    if escolha_jogador not in opcoes:
        print("---Opção inválida, escolha novamente---")
    else:
        print("---Opção válida!---")
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
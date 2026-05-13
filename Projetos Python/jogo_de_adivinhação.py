import random

secreto = random.randint(1, 10)
tentativa = 5
vitoria = 0
derrota = 0

print("\n============ JOGO DA ADIVINHAÇÃO ============")
print("Você tem 5 tentativas!\n")

try:
 while True:
    try:
        palpite = int(input("Escolha um número inteiro de 1 a 10: "))
        #Se o usuário digtar por exemplo: 100, desconta uma tentativa. Torna-se necessário não contar
        #a tentativa.
        tentativa -= 1
    except ValueError:
        print("Por favor, use somente números inteiros!\n")
        continue
 
    if palpite < 1 or palpite > 10:
        print("\nO número tem que ser entre 1 a 10!")

    elif palpite == secreto:
        vitoria += 1
        print(f"\n---Parabéns! O número secreto era {secreto}!---\n")
        print(f"--- {vitoria} Vitória, {derrota} Derrotas---\n")
        continuar = input("Gostaria tentar novamente? (S/N): ").lower()
        if continuar == "s":
            tentativa = 5
            secreto = random.randint(1, 10)
            continue
        else:
            print('Encerrando o jogo.\n')
            break
    
    elif tentativa == 0:
        derrota += 1
        print(f"\nAcabaram suas tentativas, o número secreto é {secreto}!\n")
        print(f"--- {vitoria} Vitória, {derrota} Derrotas---\n")
        continuar = input("Gostaria tentar novamente? (S/N): ").lower()
        if continuar == "s":
            tentativa = 5
            secreto = random.randint(1, 10)
            continue
        else:
            print('Encerrando o jogo.\n')
            break

    
    elif palpite < secreto:
        if tentativa == 1:
            print(f"O número é maior! Você tem {tentativa} tentativa restante\n")
        else:
            print(f"O número é maior! Você tem {tentativa} tentativas restantes\n")

    elif palpite > secreto:
        if tentativa == 1:
            print(f"O número é menor! Você tem {tentativa} tentativa restante\n")
        else:
            print(f"O número é menor! Você tem {tentativa} tentativas restantes\n")
        
except (EOFError, KeyboardInterrupt):
    print("\nJOGO ENCERRADO PELO USUÁRIO")
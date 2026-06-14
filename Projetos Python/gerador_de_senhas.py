#Gerador de senhas
import random
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def gerador_senha():
    digitos = int(input("\nQuantos caractéres sua senha terá: "))
    print("Sua senha será:")
    for s in range(digitos):
        senha = random.choice(caracteres,)
        print(f"{senha}", end="")

    print("\n")

gerador_senha()
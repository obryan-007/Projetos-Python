print("---Bem-vindo(a) a festa!!!---")

while True:

     nome = input('---Qual é o seu nome?---\n')
     idade = int(input('---Qual é a sua idade?---\n'))

     if idade < 18:
      print(f"---Sinto muito {nome}, você não tem idade o suficiente para entrar na festa---")
    
     elif idade <= 59:
      print(f"---Seja bem-vindo a festa {nome}!!!---")

     else:
      print(f"---SEJA BEM-VINDO(A) {nome} VIP!!!---")
      
     continuar = input("\nDeseja testar outro nome? (sim/nao):\n ").lower()
     if continuar != "sim":
       print("\n---Programa encerrado---")
       break
    
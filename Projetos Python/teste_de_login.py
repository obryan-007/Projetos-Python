try:
  while True:

   usuario_correto = 'Bryan'
   senha_correta = "121510"
   #inicio
   try:
     print("---ENTRAR NA CONTA---")
     print("1. Fazer login")
     print("2. Sair")
     opção = input("Escolha uma das opções: ")
   except Exception:
     print("\nOcorreu um erro, tente novamente!")
     continue
       
   if opção == "2":
     print("Encerrando programa...")
     break

   elif opção == "1":
     usuario_digitado = input("\nDigite o login: ")
     senha_digitada = input("Digite a senha: ")
     if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
        print("Login feito.")
        break
     else:
        print("Login ou senha incorretos.\n")
     decisao = input("Gostaria de tentar novamente? (s/n):")
     if decisao == "s":
        continue
     else:
        print("Encerrando programa...")
        break
        #fim
except KeyboardInterrupt:
  print("\nPrograma encerrado manualmente pelo usuário!")
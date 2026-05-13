print("---Calculadora Simples---\n")
while True:
    try:
     num1 = float(input('---Digite um número: '))
     num2 = float(input('---Digite um outro número: '))
     operação = input('---Selecione uma operação (+, -, *, /, **: ')
    except ValueError:
        print("Erro, digite apenas números")
        continue

    if operação == "+":
        print(num1 + num2)
        
    elif operação == "-":
        print(num1 - num2)
        
    elif operação == "*":
        print(num1 * num2)
    
    elif operação == "/":
        if num2 == 0:
         print("Impossível dividir outro número por 0")
        else:
         print(num1 / num2)

    elif operação == "**":
       print(num1 ** num2)
         
    else:
        print('---Operação Invalida!')
    continuar = input("---Deseja fazer outro cálculo? (s/n): ").lower()
     
    if continuar != "s":
        print("---Encerrando programa...")
        break
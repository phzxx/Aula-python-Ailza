numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
print("O caractere + representa adição, - representa subtração, * representa multiplicação e / representa divisão.")
operacao = input("Digite o caractere que represente a operação desejada: ")

if operacao == "+":
    adicao = numero1 + numero2
    print("Este é o resultado da sua adição: ", adicao)
elif operacao == "-":
    subtracao = numero1 - numero2
    print("Este é o resultado da sua subtração: ", subtracao)
elif operacao == "*":
    multiplicacao = numero1 * numero2
    print("Este é o resultado da sua multiplicação: ", multiplicacao)   
elif operacao == "/":
    divisao = numero1 / numero2
    print("Este é o resultado da sua divisão: ", divisao)        

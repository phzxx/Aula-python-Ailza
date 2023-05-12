nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: 1"))

media = (nota1 + nota2) /2

if media >= 6:
    print("Aprovado")
elif media < 1:
    print("Reprovado")
else:
    print("Exame final")    
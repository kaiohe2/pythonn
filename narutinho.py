nota1 = float(input("digite a nota 1 "))
nota2 = float(input("digite a nota 2 "))
nota3 = float(input("digite a nota 3 "))

media = (nota1 + nota2 + nota3) / 3

#verificar a media
if media >= 7:
    print("o aluno está aprovado")
elif media <= 5:
    print("o aluno esta em recuperação!")
else:
    print("o aluno foi reprovado!")
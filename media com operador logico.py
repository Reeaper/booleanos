print("Calcular a média")

n1 = int(input("Insira a nota do 1° trimestre: "))
n2 = int(input("Insira a nota do 2° trimestre: "))
n3 = int(input("Insira a nota do 3° trimestre: "))
n4 = int(input("Insira a nota do 4° trimestre: "))

print("Calculando")
media = (n1+n2+n3+n4)/4
print("Nota final",media)

if media >= 6:
    print("Parabéns,você foi aprovado")
elif media >3 and media<6:
    print("Terá que fazer o exame de recuperação")
else:
    print("Sinto muito,voê foi reprovado")
a = float(input("digite quantos minutos de internet você gostaria de usar por mês: "))

if a < 200:
    menos =int (a * 0.20)
    print("Você irá pagar R$:",menos)
if a>= 200 or a <=400:
    medio =int (a * 0.18)
    print("Você irá pagar R$:",medio)
else:
    maior =int (a * 0.15)
    print("Você irá pagar R$:",maior)
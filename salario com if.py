sal= float(input("Digite seu salário para calcular seus impostos: "))

base= sal
imposto= 0
if base> 3000:
    imposto= imposto+((base - 3000)*0.35)
    base= 3000
if base>= 1000:
    imposto= imposto +((base - 1000)*0.20)
print('Salario: R$%6.2f imposto a pagar:R$%6.2f' % (sal,imposto))
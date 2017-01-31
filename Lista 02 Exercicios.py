# Exercicio01

n1=float(input("Valor 1º lado:" ))
n2=float(input("Valor 2º lado:" ))
n3=float(input("Valor 3º lado:" ))

if n1+n2 > n3:
    if((n1==n2) and (n1==n3)):
        triangulo = "equilátero"
    elif ((n1==n2) or (n2==n3) or (n1==n3)):
        triangulo = "isosceles"
    elif n1!=n2 and n3 or n2!= n1 and n3 and n1!=n3:
        triangulo = "escaleno"
else:
    triangulo = "Não é um triangulo"

print = "Resultado: %s"%triangulo


#Exercicio 02

ano = int(input("Informe o ano:" ))

if ano%4 == 0:
    print ("Ano bissexto")
else:
    print ("Ano não bissexto")


#Exercicio 03

multa_kg = 4.00
peso = float ( input ( "Informe o peso: "))

if peso > 50.00:
    excedente = peso - 50.00 
    multa = excedente * multa_kg

else:
    excedente = 0.00
    multa = 0.00

print ("Peso excedente: %.2fkg e Multa R$%.2f" % ( excedente,multa ))


#Exercicio 04

lista =[]
x=1
while x<=3:
    lista.append (input("Informe nº: "))
    x=x+1
maior = max(lista)
print("O maior nº é %s " %maior)

#Exercicio 05

lista =[]
x=1
while x<=3:
    lista.append (input("Informe nº: "))
    x=x+1
maior = max(lista)
menor = min(lista)

print("O maior nº é %s e o menor nº é %s" %(maior, menor))

#Exercicio 06

valor_hora= float(input("Informe o valor hora: "))
horas_trab = float(input("Informe qtde de horas mês: "))
valor_bruto = valor_hora*horas_trab
#descontos
inss = valor_bruto*0.08
ir = valor_bruto*0.11
sindicato = valor_bruto*0.05

valor_liquido = valor_bruto-(inss+ir+sindicato)

print( "Salário Bruto = %.2f \nINSS = %.2f \nSindicato = %.2f" %(valor_bruto,inss,sindicato))


#Exercicio 07

m = int ( input ( "Informar a metragem (m²):" ))
if m %54!=0:
    latas = int( m/54)+1
else:
    latas= m/54

valor = latas * 80

print ( "%d lata(s) a um custo de %.2f" %(latas, valor))

''' Exercicio01
Faça um Programa que peça os três lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. '''

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


'''Exercicio 02
Determine se um ano é bissexto'''

ano = int(input("Informe o ano:" ))

if ano%4 == 0:
    print ("Ano bissexto")
else:
    print ("Ano não bissexto")


'''Exercicio 03
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. 
Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. 
Caso contrário mostrar tais variáveis com o conteúdo ZERO. '''

multa_kg = 4.00
peso = float ( input ( "Informe o peso: "))

if peso > 50.00:
    excedente = peso - 50.00 
    multa = excedente * multa_kg

else:
    excedente = 0.00
    multa = 0.00

print ("Peso excedente: %.2fkg e Multa R$%.2f" % ( excedente,multa ))


'''Exercicio 04
Faça um Programa que leia três números e mostre o maior deles. '''

lista =[]
x=1
while x<=3:
    lista.append (input("Informe nº: "))
    x=x+1
maior = max(lista)
print("O maior nº é %s " %maior)

'''Exercicio 05
Faça um Programa que leia três números e mostre o maior e o menor deles. '''

lista =[]
x=1
while x<=3:
    lista.append (input("Informe nº: "))
    x=x+1
maior = max(lista)
menor = min(lista)

print("O maior nº é %s e o menor nº é %s" %(maior, menor))

'''Exercicio 06
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, 
quanto pagou ao sindicato e o salário líquido. 
Observe que Salário Bruto - Descontos = Salário Líquido. 
Calcule os descontos e o salário líquido, conforme a tabela abaixo: 
a. + Salário Bruto : R$ 
b. - IR (11%) : R$ 
c. - INSS (8%) : R$ 
d. - Sindicato ( 5%) : R$ 
e. = Salário Liquido : R$ '''

valor_hora= float(input("Informe o valor hora: "))
horas_trab = float(input("Informe qtde de horas mês: "))
valor_bruto = valor_hora*horas_trab
#descontos
inss = valor_bruto*0.08
ir = valor_bruto*0.11
sindicato = valor_bruto*0.05

valor_liquido = valor_bruto-(inss+ir+sindicato)

print( "Salário Bruto = %.2f \nINSS = %.2f \nSindicato = %.2f" %(valor_bruto,inss,sindicato))


'''Exercicio 07
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
Obs. : somente são vendidos um número inteiro de latas'''

m = int ( input ( "Informar a metragem (m²):" ))
if m %54!=0:
    latas = int( m/54)+1
else:
    latas= m/54

valor = latas * 80

print ( "%d lata(s) a um custo de %.2f" %(latas, valor))

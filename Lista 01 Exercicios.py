#Lista01 - Exercicio01

a=int(input("Digite o 1º numero: "))
b=int(input("Digite o 2º numero: "))
soma = a + b

print(" A soma dos numeros é: %d" %soma)

#Exercicio02

a=int(input("Informe a metragem: "))
conv = a*1000

print("A metragem informada possui %d milimetros " %conv)

#Exercicio03

dias = input("Digite uma quantidade de dias: ")
horas = input("Digite uma quantidade de horas: ")
minutos = input("Digite uma quantidade de minutos: ")
segundos = input("Digite uma quantidade de segundos: ")

totalSegundos = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos

print (dias,"dias",horas,"horas",minutos,"minutos",segundos,"segundos representam", totalSegundos,"segundos")


#Exercicio04

sal = int(input("Informar salário: "))
n = float(input("Informar % de aumento: "))
aumento = n /100.0 * sal
novo = sal + aumento

print( "O aumento será de %.2f e o novo salário de R$%.2f" % (aumento,novo)
      

#Exercicio05
valor = input("Informar o valor: ")
n = float(input("Informar % de desconto: "))
desconto = n /100.0 * val
novo = val - desconto

print( "O desconto será de %.2f e o novo valor será de %.2f" % (desconto,novo))

#Exercicio06

dist=float(input("Informe a distância: "))
vel = int(input("Velocidade média: "))
tempo = dist/vel

print (" O tempo médio gasto para o percurso sera de %.2f horas" %tempo)

#Exercicio07

temp = float(input("Informe a temperatura: "))
novatemp = 9*temp/5+32
print("Temperatura em Fahrenheit: %.1f" %novatemp)
        #Ou o print pode ser assim :
print "Temperatura em Fahrenheit:", novatemp

#Exercicio08

temp = float(input("Informe a temperatura: "))
novatemp = (temp-30)/2
print "Temperatura em Celsius:", novatemp

#Exercicio09

n1 = 60
n2 = 0.15
km=float(input("Informe o km utilizado: "))
dias = int(input("Informe dias de aluguel: "))
preco = ( km*n2)+(dias*n1)
print("O valor a pagar será de R$ %.2f" %preco)

#Exercicio10 

minuto=10
quant=int(input("Quantidade de cigarros fumados por dia:  "))
anos=int(input("Informe quantos anos é fumante: "))
cigarrodia=float( quant*minuto )
perdadia=cigarrodia/(60*24)
dia= anos*365
perda = float(dia*perdadia)
print( "Você perdeu %.2f dias devido ao fumo" %perda)

#Exercicio11

x=(2**8) # Alterar o denominador aqui
y=len(str(x))

print("A quant de caracteres que contem em X é %s" %y)


       

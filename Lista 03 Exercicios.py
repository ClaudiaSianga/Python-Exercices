'''Exercicio 01
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor 
seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

numero = int(input("digite um numero de 0 a 10 ---> "))
while 0 > numero or 10 < numero:
    numero = input("Nº inválido, digite um numero de 0 a 10 ---> ")

'''Exercicio 02
Faça um programa que leia um nome de usuário e a sua senha e não
aceite a senha igual ao nome do usuário, mostrando uma mensagem de
erro e voltando a pedir as informações. '''

usuario = input ("Informe usuário: ")
senha = input ("Informe a senha: ")
if usuario == senha:
    senha = input ("Senha Inválida, digite outra senha: ")
    if usuario !=senha:
        print ("Senha cadastrada!")

'''Exercicio 03
Supondo que a população de um país A seja da ordem de 80.000 habitantes com
uma taxa anual de crescimento de 3% \e que a população de B seja 200.000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento'''

a = 80000
b = 200000
ano = 0

while a <= b:
	a += a * 0.03
	b += b * 0.015
	ano += 1

print ( "O Pais A ultrapassa ou iguala o Pais B em %d anos" %ano )

''' Exercicio 04
A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
Sua regra de formação é simples: os dois primeiros elementos são 1; a partir
de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que
leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1,
F3 = 2, etc.
'''

fibo = [1,1]
i = 0
num = int(input("Entre com um número: "))

while num > len(fibo):
	fibo.append(fibo[i] + fibo[i+1])
	i+=1

print ('Fibonacci(%d): %d' %(num,fibo[num-1]))

'''Exercicio 05

Dados dois números inteiros positivos, determinar o máximo divisor comum
entre eles usando o algoritmo de Euclides. '''

print("Determina o mdc de dois números n > 0 e m > 0\n")

# leia o valor de n
n = int(input("Digite o valor de n (n > 0): "))

# leia o valor de m
m = int(input("Digite o valor de m (m > 0): "))

# em cada iteração mdc é o candidato a mdc(n,m)
mdc = n
while n % mdc != 0 or m % mdc != 0: 
    mdc = mdc - 1

print("MDC(%d,%d)=%d" %(n,m,mdc))


















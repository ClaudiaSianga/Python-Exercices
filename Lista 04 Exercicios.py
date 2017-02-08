'''Exercicio01
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra
o maior e o menor valor, sem usar as funções max e min'''

import random
lista=[]
maior = 0
menor = 100
while len(lista) < 10:
    x = random.randint ( 1,100)
    if x not in lista:
        lista. append (x)

    if x<menor:
        menor = x

    if x>maior:
        maior = x
lista.sort()

print("="*40)
print ( lista )
print ("Menor é %d e o Maior é %d" %(menor, maior))
print("="*40)


'''Exercicio02
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os
números pares na lista PAR e os números ímpares na lista
IMPAR. Imprima as três listas.'''

import random
lista=[]
lista_par=[]
lista_impar=[]
while len(lista) < 20:
    x = random.randint ( 1,100)
    if x not in lista:
        lista. append (x)

    if x%2==0:
        lista_par.append(x)
    else:
        lista_impar.append(x)
        
lista.sort()
lista_par.sort()
lista_impar.sort()

print("="*40)
print (lista)
print("Num. Pares %s" %lista_par)
print("Num. Ímpares %s" %lista_impar)
print("="*40)

'''Exercicio03
Faça um programa que crie dois vetores com 10 elementos
aleatórios entre 1 e 100. Gere um terceiro vetor de 20
elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores.
Imprima os três vetores. '''

import random
lista1 = []
lista2 = []
lista3 = []

while len(lista1) < 10:
    numero = random.randint(1,100)
    if numero not in lista1:
        lista1.append(numero)
        lista3.append(numero)


while len(lista2)  < 10:
    numero = random.randint(1,100)
    if numero not in lista2:
        lista2.append(numero)
        lista3.append(numero)

lista1.sort()        
lista2.sort()
lista3.sort()

print ("Lista A %s" %lista1)
print ("Lista B %s" %lista2)
print (lista3)

'''Exercício04
Seja o statement sobre diversidade:
“The Python Software Foundation and the global Python community welcome
and encourage participation by everyone. Our community is based on mutual
respect, tolerance, and encouragement, and we are working to help each other
live up to these principles. We want our community to be more diverse: whoever
you are, and whatever your background, we welcome you.”. Gere uma lista de
palavras deste texto com split(), a seguir crie uma lista com as palavras
que começam ou terminam com uma das letras “python”.
Imprima a lista resultante. Não se esqueça de remover antes os caracteres
especiais e cuidado com maiúsculas e minúsculas.'''

lista1=[]
lista2=[]

lista1 = '''The Python Software Foundation and the global Python community welcome
and encourage participation by everyone. Our community is based on mutual
respect, tolerance, and encouragement, and we are working to help each other
live up to these principles. We want our community to be more diverse: whoever
you are, and whatever your background, we welcome you'''

lista1 = lista1.lower()

lista1=lista1.replace("ç","c")
lista1=lista1.replace("á","a")
lista1=lista1.replace("á","a")
lista1=lista1.replace(":"," ")
lista1=lista1.replace(","," ")
lista1=lista1.replace("."," ")

lista1 = lista1.split()

for x in lista1:
    y = x.lower()
    if y[0] in"python" or y[-1] in "python":
        lista2.append(x)


print("lista 1 (TOTAL): %s" %lista1)
print("lista 2 (PYTHON): %s" %lista2)

'''Exercicio05
Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das
letras “python” e que tenham mais de 4 caracteres. Não se esqueça de
transformar maiúsculas para minúsculas e de remover antes os caracteres
especiais.'''


lista1=[]
lista2=[]

lista1 = '''The Python Software Foundation and the global Python community welcome
and encourage participation by everyone. Our community is based on mutual
respect, tolerance, and encouragement, and we are working to help each other
live up to these principles. We want our community to be more diverse: whoever
you are, and whatever your background, we welcome you'''

lista1 = lista1.lower()

lista1=lista1.replace("ç","c")
lista1=lista1.replace("á","a")
lista1=lista1.replace("á","a")
lista1=lista1.replace(":"," ")
lista1=lista1.replace(","," ")
lista1=lista1.replace("."," ")

lista1 = lista1.split()
maior = 0

for x in lista1:
    y = x.lower()
    if y[0] in"python" or y[-1] in "python" and len (y) >4:
        lista2.append(x)
        if(len(x) > 4):
            maior = maior+1
            
    
   
print("lista 1 (TOTAL): %s" %lista1)
print ("\n\n", "="*40)
print ("lista 2 (PYTHON): %s" %lista2)
print ("\n\n", "="*40)
print ("Quantidade total da lista 2: %d" %maior)









































    

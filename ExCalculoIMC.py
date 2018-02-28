import math
#Exercícios Extras - 6 - Aula 6
#Autor : Victor Forato
#Data : 23/03

#Dados
peso = int(input("Insira seu peso em kg : "))
altura = float(input("Insira sua altura em metros : "))

#Processamento
imc = peso/math.pow(altura,2)

if imc<20 :
    print("Seu IMC está abaixo de 20, ou seja, você está abaixo do peso ! ")
if imc>20 and imc<25 :
    print("Seu IMC está entre 20 e 25, ou seja, seu peso está normal ! ")
if imc>25 and imc<30:
    print("Seu IMC está entre 25 e 30, ou seja, você está com excesso de peso ! ")
if imc>30 and imc<35:
    print("Seu IMC está entre 30 e 35, ou seja, você é considerado Obeso ! ")
if imc>35:
    print("Seu IMC está acima de 35, ou seja, sua situação é considerada como Obesidade Mórbida ! ")


input("Tecle qualquer letra ou número para fechar o programa ! ")


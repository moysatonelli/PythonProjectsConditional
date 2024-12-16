#O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso.
#Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula:
#IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).

peso = float(input("Digite o peso:  "))
altura = float(input("Digite a altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 18.5 and imc <= 25:
    print("Peso normal")
elif imc >= 25:
    print("Sobrepeso")
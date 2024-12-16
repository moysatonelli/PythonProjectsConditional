#Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar.
#Essa verificação será usada para definir ações diferentes dentro do jogo.
#Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.

paridade = int(input("Digite um número inteiro: "))
if paridade % 2 == 0:
    print(f"\nO número {paridade} é par")
else:
    print(f"\nO número {paridade} é ímpar")
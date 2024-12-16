#Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados.
#As regras são:
#Média >= 7: Aprovado
#5 <= Média < 7: Recuperação
#Média < 5: Reprovado
#Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.
from unittest import case

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nMédia: {media:.2f}")

match media:
    case media if media < 5:
        print("Reprovado")
    case media if 5 <= media < 7:
        print("Recuperação")
    case media if media >= 7:
        print("Aprovado")


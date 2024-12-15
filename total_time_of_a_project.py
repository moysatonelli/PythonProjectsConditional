#se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

print("Calculando o tempo total:\n")

a = int(input("Informe os dias para a atividade A: "))
b = int(input("Informe os dias para a atividade B: "))
c = int(input("Informe os dias para a atividade C: "))

if a < 0 or b < 0 or c < 0:
    print("\nOs dias não podem ser negativos")
else:
    soma = a + b + c
    print(f"\nO total de dias para as atividades A, B e C são: ({soma}) dias")
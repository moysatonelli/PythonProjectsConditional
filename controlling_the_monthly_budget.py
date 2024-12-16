#Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos.
#Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas.
#O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

despesas = float(input("Digite o valor de despesas do mês: "))

if despesas > 3000.00:
    print(f"\nAtenção! Você ultrapassou o limite do orçamento.\nO limite para seus gatos é de R${3000.00:.2f}")
else:
    print("O limite dos gastos está dentro do limite esperado.")
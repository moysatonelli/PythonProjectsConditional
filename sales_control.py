#Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais.
#Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

maca = int(input("Digite a quantidade de maçãs vendidas: "))
banana = int(input("Digite a quantidade de bananas vendidas: "))

if maca > banana:
    print(f"Maça foi a mais vendida: {maca}(UN)")
elif maca == banana:
    print(f"Houve um empate! Maçãs: {maca}(UN) | Bananas: {banana}(UN)")
elif maca < banana:
    print(f"Banana foi a mais vendida: {banana}(UN)")
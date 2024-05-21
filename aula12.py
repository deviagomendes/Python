v1 = float(input("Digite o valor do produto: "))
d = int(input("Digite a quantidade de desconto: "))
print("O desconto de {}% em cima de R${:.2f} é R${:.2f}, sendo assim você pagará R${:.2f}".format(d, v1, v1*(d/100), v1 - (v1*(d/100))))
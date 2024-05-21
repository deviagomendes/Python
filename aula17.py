co = int(input("Digite o valor do cateto oposto: "))
ca = int(input("Digite o valor do cateto adjacente: "))
h = ((co**2) + (ca**2))**0.5

print("A hipotenusa desse triângulo é: {:.1f}".format(h))
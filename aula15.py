custokm = 0.15
custodia = 60
dias = float(input("Quantos dias você viajou com o carro? "))
km = float(input("Qual a quantidade de KM's percorridos com o veículo? "))

total = (custokm*km)+(custodia*dias)

print("Foram percorridos {} km's por {} dias, sendo assim, você pagará R${:.2f}. Considerando que o custo por dia é de R${:.2f} e o valor por KM rodado é de R${:.2f}".format(km, dias, total, custodia, custokm))
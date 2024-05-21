salario_atual = float(input("Digite aqui o salário do colaborador em R$: "))
aumento = float(input("Digite em quantos % você deseja aumentar o salário dele: "))
total = (salario_atual*(aumento/100))

print("O aumento será de R${:.2f}, sendo assim o salário passará de R${:.2f} para R${:.2f}".format(total, salario_atual, salario_atual+total))
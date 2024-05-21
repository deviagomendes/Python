lp = float(input("Digite a largura da parede: "))
ap = float(input("Digite a altura da parede: "))
lt = 2
area = lp * ap
print("Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m²".format(lp, ap, area))
print("Para pintar essa parede será necessário {:.2f} litros de tinta".format((lp*ap)/lt))
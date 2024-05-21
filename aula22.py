n = str(input("Digite seu nome completo: "))
separa_n = n.split( )
primeiro_n = separa_n[0]
completo_n = ''.join(separa_n)
print("Analisando seu nome......")
print("Seu nome em MAIÚSCULAS:",n.upper())
print("Seu nome em MINÚSCULAS:",n.lower())
print("Seu nome tem ao todo: {} letras".format(len(completo_n)))
print("Seu primeiro nome é {} e ele tem {} letras".format(primeiro_n, len(primeiro_n)))

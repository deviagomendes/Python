from random import shuffle

pessoa1 = input("Digite o nome da primeira pessoa: ")
pessoa2 = input("Digite o nome da segunda pessoa: ")
pessoa3 = input("Digite o nome da terceira pessoa: ")
pessoa4 = input("Digite o nome da quarta pessoa: ")

pessoas = [pessoa1, pessoa2, pessoa3, pessoa4]

shuffle(pessoas)

print("A ordem será: {}".format(pessoas))
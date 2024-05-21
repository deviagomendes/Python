n = input("Digite uma sequência de números separados por vírgula(SEM ESPAÇO): ").strip()
k = int(input("Digite qual será o múltiplo número: "))
number = ''
lista = []
multiplos = []
multiplosOrg = []

#Transformando a entrada do usuário em uma lista
for x, i in enumerate(n):
    if i != ",":
        number += i
    else:
        lista.append(number)
        number = ''

if x == len(n) - 1:
    lista.append(number)

for i in lista:
    transform = int(i)%k
    if transform == 0:
        multiplos.append(i)

multiplos.sort()

multiplos = ", ".join(map(str, multiplos))


print("Os múltiplos de {} são {}".format(k, multiplos))

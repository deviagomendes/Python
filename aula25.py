# Encontre a palavra do input dentro de uma frase e a posição da palavra dentro do texto.

# frase = str(input("Digite uma palavra: "))
# palavra = str(input("Digite o que deseja procurar: "))
# t_lista = frase.split(" ")
# try:
#     busca = t_lista.index(palavra)
#     print("Está presente na frase e se encontra na {}ª palavra".format(busca + 1))
# except:
#     print("Não há palavra")


frase = str(input("Digite uma frase: ").lower())
busca = str(input("Digite o que deseja procurar: ").lower())
palavra = ''
vet = []
for n,i in enumerate(frase):
    if i != ' ':
        palavra += i
    else:
        vet.append(palavra)
        palavra = ''   
    if n == len(frase)-1:
        vet.append(palavra)

for nn,z in enumerate(vet):
    if z == busca:
        pos = nn

try:
    print("Sua palavra está na {}ª palavra e sua frase tem {} palavras".format(pos+1, nn+1))
except:
    print("Não essa há palavra")
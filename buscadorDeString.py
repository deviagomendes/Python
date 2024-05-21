frase = str(input("Digite uma frase: ").lower())
buscarPalavra = str(input("Digite uma palavra para buscar: ").lower())
palavra = ''
arr = []
Npalavra = ''

for i in buscarPalavra:
    if i != ' ':
        Npalavra += i

for n, i in enumerate(frase):
    if i != ' ':
        palavra += i
    else:
        arr.append(palavra)
        palavra = ''
    if n == len(frase)-1:
        arr.append(palavra)

for nn, pos in enumerate(arr):
    if Npalavra == pos:
        indice = nn
        
try:
    if indice != -1:
        print("A palavra '{}' está na {}ª posição e o texto contém {} palavras".format(Npalavra, indice+1, len(arr)))
except:
    print("Não há essa palavra na frase")
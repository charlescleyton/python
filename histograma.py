# lista = list(input("Informe uma lista de caracteres: "))
# histograma = dict()
# for char in lista:
#     contador = histograma.get(char.lower(),0)
#     histograma.update({char.lower() : contador + 1})
# print(histograma)

from os import strerror

try:
	hist = dict()
	for line in open('text.txt', 'rt'):
		for ch in line:
		    print(ch, end='')
		    if ch != '.' and ch != '\n' and ch != ' ':
			    hist[ch.lower()] = hist.get(ch.lower(), 0) + 1
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
	
print("\n\nHistograma:\n")
for chave in sorted(hist.keys()):
    print(f'{chave} -> {hist[chave]}')   
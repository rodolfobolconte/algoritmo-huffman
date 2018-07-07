#cabeçalhos de todos os programas
from heapq import heappush, heappop, heapify
import collections
from io import StringIO

# função do codificador de Huffman
def encode(simbolos_e_frequencia):
	#Huffman encode the given dict mapping symbols to weights
	#Huffman codifica os símbolos de mapeamento dict para pesos

	lista_de_prioridade = [[repeticao, [simbolo, ""]] for simbolo, repeticao in simbolos_e_frequencia.items()]

	heapify(lista_de_prioridade)

	while len(lista_de_prioridade) > 1:

		primeiro_item = heappop(lista_de_prioridade)
		segundo_item = heappop(lista_de_prioridade)

		for pair in primeiro_item[1:]:
			pair[1] = '0' + pair[1]

		for pair in segundo_item[1:]:
			pair[1] = '1' + pair[1]

		heappush(lista_de_prioridade, [primeiro_item[0] + segundo_item[0]] + primeiro_item[1:] + segundo_item[1:])

	return sorted(heappop(lista_de_prioridade)[1:], key=lambda p: (len(p[-1]), p))

def convert(frase, bits):

	frase_codificada = ''

	for caractere in frase:
		for bit in bits:
			if caractere == bit[0]:
				frase_codificada += bit[1]

	return frase_codificada

def decode(frase_codificada, bits):
	
	frase_decodificada = ''

	temporario = ''

	inicio = 0

	for caractere in range(len(frase_codificada) + 1):
		igual = 0
		for bit in bits:
			if frase_codificada[inicio:caractere] == bit[1] and inicio != len(frase_codificada) - 1:
				igual += 1
				temporario = bit[0]

			elif frase_codificada[inicio:caractere] == bit[1] and inicio == len(frase_codificada) - 1:
				igual += 1
				temporario = bit[0]

		if igual == 1:
			frase_decodificada += temporario
			inicio = caractere
		else:
			continue

	return frase_decodificada


# teste dessa função do codificador de Huffman, usando uma maneira simplória de implementar isso para um texto pequeno.
frase = "frase a ser codificada"

simbolos_e_frequencia = collections.Counter(frase)

bits = encode(simbolos_e_frequencia)
frase_codificada = convert(frase, bits)
frase_decodificada = decode(frase_codificada, bits)


print("Frase Original:", frase)
print("Frase Codificada:", frase_codificada)
print("Frase Decodificada:", frase_decodificada)


print("\nTabela Caractere-Bit:")
print("Symbol\tWeight\tHuffman Code")
for p in bits:
	print ("%s\t\t%s\t\t%s" % (p[0], simbolos_e_frequencia[p[0]], p[1]))
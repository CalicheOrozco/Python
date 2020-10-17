import csv
from random import randrange, randint


def NuncaNuncaRandom(i):
	#Crea la lista vacia
	frase = []
	#Abre el csv donde estan los yo nunca nunca
	with open('yoNuncaNunca.csv') as File:
	    reader = csv.DictReader(File, delimiter='.')
	    #Recorre cada columna y la agrega a la lista
	    for row in reader:

	        frase.append(row)


	    #retorna la frase del numero porporcionado
	    return frase[i]['Frases']

nuncanunca = NuncaNuncaRandom(randrange(0, 345))
print(nuncanunca)
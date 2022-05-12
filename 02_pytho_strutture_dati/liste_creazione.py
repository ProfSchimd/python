# literal
lista1 = [1, 2, 3]
listaVuota = []
listaZeri = [0]*5 # [0, 0, 0, 0, 0]
listaZeriUni = [0,1]*2 # [0, 1, 0, 1]
tantiZeri = listaZeri*10
# conversione
listaNumeri = list(range(100)) # da 0 a 99
altraLista = list(listaNumeri) # copia la lista!
stessaLista = listaNumeri # copia il riferimento!
# list comprehension
ulterioreLista = [i for i in range(100)] # da 0 a 99
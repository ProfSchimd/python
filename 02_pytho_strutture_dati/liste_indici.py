lista = list(range(10)) # [0, 1, ..., 9]
print(lista[0:3]) # elementi dalla posizione 0 (inclusa) alla 3 (esclusa) [0, 1, 2]
print(lista[:3]) # lo stesso (quando l'inizio è 0 si può omettere)
print(lista[2:4]) # elementi dalla posizione 2 (inclusa) alla 4 (esclusa) [2, 3]
print(lista[3::]) # elementi dalla posizione 3 alla fine [3, 4, 5, ..., 9]
print(lista[:]) # stampa tutta la lista (anche lista[::])
print(lista[0:5:2]) # da posizione 0 a 5 (esclusa) a salti di due [0, 2, 4]
print(lista[::3]) # tutta la lista a salti di 3 [0, 3, 6, 9]
print(lista[-1]) # 9 (no lista, ma numero!)
print(lista[-3:-1]) # Attenzione! [7, 8] non [8, 9] e non [7, 8, 9]
print(lista[-3::]) # Ultimi tre elementi [7, 8, 9]
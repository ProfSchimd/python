import random

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

difficultiesNames = ["Molto Bassa","Bassa","Normale","Media","Alta"]
print ("Benvenuti su Indovina il numero!!")

nome = input("Scrivi il tuo nome: ")
print ("Iniziamo a giocare " + nome + "!!")
try:
    dif = int(input("Seleziona una difficoltà tra 1 e 5: "))
except:
    print("input non valido")
    dif = -1
while (dif < 0) or (dif > 5):
    try:
        dif = int(input("La difficoltà deve essere 1,2,3,4 o 5: "))
    except:
        print("input non valido")
        dif = -1
print("Difficoltà selezionata:", difficultiesNames[dif - 1])
path = "classifica.csv"
# Bene!
n = random.randint(10 ** (dif - 1), 10 ** (dif) - 1)
t = 0
victory = False
guess = "-1"
print()
while(guess != str(n) and guess != "q"):
    t+=1
    print("Tentativi " + str(t))
    guess = input(nome + ", prova a indovinare il mio numero:")
    if(guess != "q"):
      try:
          if(int(guess) > n):
              print("Scusa, numero troppo in alto!\nProva con un numero più piccolo")
          elif(int(guess) < n):
              print("Scusa, numero troppo piccolo!\nProva con un numero più alto")
          else:
              victory = True
      except:
          print("input non valido, riprovare")
          guess = -1
          t-=1
      print()
if(victory):
    print(nome + " ha vinto dopo " + str(t) + " tentativi!")
else:
    print("Puoi farcela la prossima volta!")

if(victory):
  file = open(path, "a")
  file.write(nome + ";" + str(t) + ";" + str(dif) + "\n")
  file.close()
  file = open(path, "r")
  nRiga = 0
  for riga in file:
    if(riga.split(";")[2] == str(dif)+ "\n"):
      nRiga+=1

  file.close
  tupleList = list(range(nRiga))

  i = 0
  file = open(path)
  for riga in file:
    if(riga.split(";")[2] == str(dif)+ "\n"):
      tupleList[i] = tuple(riga.split(";"))
      i+=1
  file.close
  for l in range(len(tupleList)):
    for j in range(l, len(tupleList)):
      if(int(tupleList[l][1]) > int(tupleList[j][1])):
        aux = tupleList[l]
        tupleList[l] = tupleList[j]
        tupleList[j] = aux
  print(tupleList)
print("")
print("********************************")
print("*     Scoreboard","(", dif, ")", "        *")
print("********************************")
print()
print("+------------------------------+")
print("| Pos\tName\tAttempts       |")
print("+------------------------------+")
for l in range(10):
  try:
    print("|",l+1,"\t"+tupleList[l][0]+"\t"+str(tupleList[l][1]+"\t|"))
  except:
    print("|",l+1,"---------------------------- |")

print("+------------------------------+")

# In generale il programma è fatto bene, ci sono alcune cose da migliorare
# sopratutto l'uso dei commenti ed il nome delle variabili che non sono
# un grosso problema (ma piccolo) in un programma di 100 righe, ma quando
# i programmi diventano grandi è fondamentale avere commenti e nomi di
# variabili scelti bene. Anche l'uso di funzioni per le varie parti
# sarebbe stato utile per la comprensione (e per la qualità del codice,
# come già ho scritto sopra)

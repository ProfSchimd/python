import random

# In generale è sempre buona norma dividere i file in
# funzioni anche se sono semplice. Questo permette poi
# di cambiare le cose in modo più semplice e veloce.
# Inoltre, quando il codice è diviso in pezzi più piccoli
# è più facile fare il 'debug' per trovare errori.

difficultiesNames = ["Neonato","Novellino","Agonista","Esperto","Maestro"]
print ("Benvenuti su Indovina il numero!!")

name = input("Scrivi il tuo nome: ")
print ("Iniziamo a giocare "+ name+"!!")
try:
    difficulty = int(input("Seleziona una difficoltà tra 1 e 5: "))
except:
    print("input non valido")
    difficulty = -1
while (difficulty < 0) or (difficulty > 5):
    try:
        difficulty = int(input("La difficoltà deve essere 1,2,3,4 o 5: "))
    except:
        print("input non valido")
        difficulty = -1
print("Difficoltà selezionata:" , difficultiesNames[difficulty-1])
path = "classifica.txt"
number = random.randint(10**(difficulty-1),10**(difficulty)-1)
t = 0
victory = False
# Non mi piace molto l'idea che tu usi le stringhe per indovinare
# e continui a convertire interi in stringhe e stringhe in interi
# sarebbe stato meglio lavorare solo con gli interi in questo caso
# gli 'if' sotto per vedere se il guess è maggiore o minore sarebbe
# stato anche più 'pulito', ad esempio
#   if(guess > number):
# aziché
#   if(int(guess) > number):

guess = "-1"
print()
while(guess != str(number) and guess != "q"):
    t+=1
    print("Tentativi " + str(t))
    guess = input(name + ", prova a indovinare il mio numero:")
    if(guess != "q"):
      try:
          if(int(guess) > number):
              print("Scusa, ma sei andato troppo in alto!")
          elif(int(guess) < number):
              print("Scusa, ma sei andato troppo in basso!")
          else:
              victory = True
      except:
          print("input non valido, riprovare")
          guess = -1
          t-=1
      print()
if(victory):
    print(name + " ha vinto dopo " + str(t) + " tentativi!") 
else:
    print("Puoi farcela la prossima volta!")

if(victory):
  f = open(path,"a")
  f.write(name+","+str(t)+","+str(difficulty)+"\n")
  f.close()
  f = open(path,"r")
  numberRows = 0
  for row in f:
    if(row.split(",")[2] == str(difficulty)+"\n"):
      numberRows+=1

  f.close
  tupleList = list(range(numberRows))

  i = 0
  f = open(path)
  for row in f:
    if(row.split(",")[2] == str(difficulty)+"\n"):
      tupleList[i] = tuple(row.split(","))
      i+=1
  f.close
  for l in range(len(tupleList)):
    for j in range(l, len(tupleList)):
      if(int(tupleList[l][1]) > int(tupleList[j][1])):
        aux = tupleList[l]
        tupleList[l] = tupleList[j]
        tupleList[j] = aux
  print(tupleList)
print("")
print("********************************")
print("*     Scoreboard","(",difficulty, ")", "        *")
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
# sopratutto l'uso dei commenti e la mancanza di funzioni. Questi non sono
# un grosso problema (ma piccolo) in un programma di 100 righe, ma quando
# i programmi diventano grandi sono fondamental.

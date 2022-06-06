from random import randrange

# siccome in Python non c'e' il main, spesso si vedono queste cose...
# però è sempre bene mettere tutte le istruzioni insieme e magari dopo
# aver dichiarato le varie funzioni (come si fa in C e C++ ad esempio).
# Questo permette di avere file più ordinati ed è anche più facile
# trovare gli errori.

nomeGioco = "Guess a Number"
nomiLivelli = ["Neofita", "Principiante", "Intermedio", "Maestro", "Gran maestro"]

testoBenvenuto = "Welcome to " + nomeGioco
benvenutoAsciiArt = "+" + "-" * (len(testoBenvenuto) + 2) + "+"
print (benvenutoAsciiArt)
print ("| " + testoBenvenuto + " |")
print (benvenutoAsciiArt)

while True:
    nomeUtente = input("Inserisci il tuo Nickname: ")
    if len(nomeUtente) > 0:
        break;
    print("Inserisci un nickname valido!")

diff = input(f"Benvenuto {nomeUtente}! Per iniziare a giocare, inserisci la difficoltà da 1 a 5: ")
try:
    diff = int(diff)
# nei casi sotto avresti potuto essere meno "brutale"
# e chiedere di reinserire il livello anziche' terminare
# il gioco
except:
    print("Non hai inserito un valore valido")
    exit()

if diff < 1 or diff > 5:
    print("La difficoltà dev'essere compresa tra 1 e 5!")
    exit()

print("Hai scelto la difficoltà: " + nomiLivelli[diff - 1])

# sospetto un bel Google qui! Mi starebbe bene se ci
# fosse una bella speigazione (commento), ma non c'e' niente.
numero = randrange(0 if diff == 1 else 1, 9, 1)
for i in range(1, diff):
    numero = numero * 10 + randrange(0, 9, 1)
    
tentativi = 1
giocoAttivo = True

while giocoAttivo:
    print("Tentativo numero: " + str(tentativi))
    numeroTentato = input("Prova ad indovinare il numero: ")
    try:
        numeroTentato = int(numeroTentato)
    except:
        if numeroTentato == "q":
            print("Sei uscito dal gioco")
            giocoAttivo = False
        else:
            print("Devi inserire un numero!")
        continue

    if numeroTentato < numero:
        print("Il numero è più alto")
    
    elif numeroTentato > numero:
        print("Il numero è minore")
    
    else:
        print(f"Congratulazioni {nomeUtente}, hai vinto (" + str(tentativi) + " tentativi)!")
        giocoAttivo = False
    
    tentativi += 1

tentativi-= 1

# va bene, ma c'è anche modo di farlo con un solo file
nomefile = "classifica" + str(diff) + ".txt"

file = open(nomefile, "a")
file.write(nomeUtente + "," + str(tentativi) + "\n")
file.close()


file = open(nomefile, "r")
classifica = []
for linea in file.readlines():
    dati = linea.split(',')
    classifica.append((dati[0], int(dati[1])))

# e' buona norma scrivere le funzioni sempre all'inizio del file
def usaTentativi(coppia):
    return coppia[1]

classifica.sort(key=usaTentativi)

for  i, record in enumerate(classifica):
    if(record == (nomeUtente, tentativi)):
        posizione = i
        
        
print('*' * 28)
print('*' + ' ' * 6 + 'Scoreboard (' + str(1) + ')' + ' ' * 6 + '*')
print('*' * 28)

print('+' + '-' * 26 + '+')
print('|' +  'Pos  Name        Attempts ' + '|')
print('+' + '-' * 26 + '+')

for pos, record in enumerate(classifica[0:10]):
    nome, punteggio = record
    punteggio = str(punteggio)
    print('| ' + str(pos + 1) + ('  ' if pos == 9 else '   ') + nome + ' ' * (12 - len(nome)) + punteggio + ' ' *( 9 - len(punteggio)) + '|' )

print('+' + '-' * 26 + '+')


while giocoAttivo:
    print("Tentativo numero: " + str(tentativi))
    numeroTentato = input("Prova ad indovinare il numero: ")
    tentativi += 1
    try:
        numeroTentato = int(numeroTentato)
    except:
        if numeroTentato == "q":
            print("Sei uscito dal gioco")
            giocoAttivo = False
        else:
            print("Devi inserire un numero!")
        continue

    if numeroTentato == numero:
        print(f"Congratulazioni {nomeUtente}, hai vinto!")
        giocoAttivo = False
    else:
        print("Il numero scelto è sbagliato, riprova")
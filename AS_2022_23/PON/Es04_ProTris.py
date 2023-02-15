livello = -1
inputNonValido = True
while inputNonValido:
    livello = int(input('Livello di difficoltà (3-9)? '))
    if (livello >= 3) and (livello <= 9):
        inputNonValido = False
    else:
        print('Inserisci un livello valido')    
    
nCaselle = livello**2

print('+------'*livello + '+')
for i in range(livello):
    print('|      '*livello + '|')
    print('|      '*livello + '|')
    print('|      '*livello + '|')
    print('+------'*livello + '+')

fineGioco = False
inputNonValido = True
while not fineGioco:
    while inputNonValido:
        numero = int(input('Inserisci il numero di casella: '))
        if (numero >= 0) and (numero < nCaselle):
            inputNonValido = False
        else:
            print('Numero non valido!')
    print(f'Hai scelto la casella {numero}')
    inputNonValido = True 

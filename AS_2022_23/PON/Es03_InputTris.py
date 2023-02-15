inputNonValido = True
numero = -1
while inputNonValido:
    numero = int(input('Inserisci il numero di casella: '))
    if (numero >= 0) and (numero <= 8):
        inputNonValido = False
    else:
        print('Numero non valido!')
        
print(f'Hai scelto il numero {numero}')

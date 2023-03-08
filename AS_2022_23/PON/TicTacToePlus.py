import math

def read_input(valid, msg, error):
    invalidInput = True
    number = -1
    while invalidInput:
        number = int(input(msg))
        if number in valid:
            invalidInput = False
        else:
            print(error)
    return number
    

def draw_board(board):
    edge = int(math.sqrt(len(board)))
    e = '+-------'
    s = e*edge + '+\n'
    for i in range(edge):
        s += '|' + '       |'*edge + '\n|'
        for j in range(edge):
            s += f'{board[j+edge*i]:^7}|'
        s += '\n|' + '       |'*edge + '\n'
        s += e*edge + '+\n'
    return s

def main():
    level = read_input([3,4,5,6,7,8,9], 'Inserisci il livello di difficoltà: ', 'Valore inserito non valido')
    places = list(range(level*level))
    board = places
    playing = True
    player = 'A'
    while playing:
        print(draw_board(board))
        print(f'È il turno del giocatore {player}')
        choice = read_input(places, 'Scegli una casella ', 'Casella non valida')
        board[choice] = player
        if player == 'A':
            player = 'B'
        else:
            player = 'A'
        
    
    

if __name__ == "__main__":
    main()
#1-create 3 righe da 3 spazi vuoti
#2-creare 2 turni e scelta per "X" e "O"
#3-chiedere input dove si vuole mettere la croce o il cerchio---check per input entro 1-9 e che sia integer
#4-sostituire il marker nella board
#5-update display con nuovo input da giocatore 2
#6-passare il turno al giocatore successivo e poi tornare indietro
#7-stabilire win condition e stop se raggiunta

from IPython.display import clear_output

def display(board):
    clear_output()
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-----")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-----")
    print(board[7]+"|"+board[8]+"|"+board[9])


def choose_marker():
    marker = ''

    while marker != 'X' and marker != 'O':

        marker = input("Player1, please select 'X' or 'O' to play: ").upper()

        player1 = marker
        if player1 == 'X':
            player2 = 'O'
        if player1 == 'O':
            player2 = 'X'

    print(f"Player1 is {player1}, Player2 is {player2}")
    return [player1, player2]


def choose_position():
    position = "WRONG"
    accepted_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    within_range = False

    while position.isdigit() == False or within_range == False:
        position = input("Choose a position for your marker (where 1 is the top left, 9 is the bottom right): ")

        if position.isdigit() == False:
            print("Sorry, this is not a number")
        elif int(position) not in accepted_values:
            print("Number is out of range (1-9)")
        else:
            break
    return int(position)


def game():
    # win conditions still to be set...

    # define board
    tic_tac_toe_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    already_taken = []
    # ask for marker
    players = choose_marker()

    turno = 0

    while len(already_taken) < 9:
        position = int(choose_position())
        if position in already_taken:
            print("Sorry, position already taken, choose another position")
        else:
            already_taken.append(position)
            tic_tac_toe_board.pop(position)
            tic_tac_toe_board.insert(position, players[0])
            print(tic_tac_toe_board)
            display(tic_tac_toe_board)
            players[0], players[1] = players[1], players[0]
        turno += 1
    print(already_taken)
    print(tic_tac_toe_board)

if __name__ == '__main__':
    game()
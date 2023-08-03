from board import Board
from agents import Player
from agents import AI
import sys

PLAYER_FIRST = False


def start_game():
    welcome_msg = "\n\nWelcome to Tic Tac Toe! (enter Q to quit)\n"
    welcome_msg += "------------------------------------------\n"
    welcome_msg += "\nYou be X, I'll be O.\n"
    welcome_msg += "\nDo you want to go first (y\\n)\n"
   
    response = input(welcome_msg)
    if response == "Q":
        sys.exit()
    global PLAYER_FIRST
    PLAYER_FIRST = True if response == "y" or response == "yes" else False
    print("\nVery well let's begin...\n")


def game_loop(first_player,second_player,board):

    current_player, next_player = first_player, second_player
    board.render()

    while(True):
        current_player.play()
        board.render()

        if (board.find_winner() != "None"):
            return board.find_winner()
        
        current_player, next_player = next_player, current_player

def main():
        board = Board()
        player = Player(board)
        computer = AI(board)

        start_game()

        first_player = player if PLAYER_FIRST == True else computer
        second_player = computer if PLAYER_FIRST == True else player

        winner = game_loop(first_player,second_player,board)

        winmsg = "\nThe " + winner + " was the winner!\n" if winner != "Tie" else "It's a tie!\n"
        print(winmsg)

        response = input("Would you like to play again? (y\\n)")
        if response == "y" or response == "yes":
            del board
            del player
            del computer
            main()
        else:
            sys.exit()


if __name__ == "__main__":
    main()

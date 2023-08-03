from board import Board
from random import randint
import sys

class Player:


    def __init__(self,board):
        self.board = board
        self.input_dic = {
                "q" : (0,0),
                "w" : (0,1),
                "e" : (0,2),
                "a" : (1,0),
                "s" : (1,1),
                "d" : (1,2),
                "z" : (2,0),
                "x" : (2,1),
                "c" : (2,2)
                }



    def get_input(self):

        while(True):
            x = input("\nYour move... \n")
            if x == "Q":
                sys.exit()
            if x in self.input_dic:
                return self.input_dic[x]
            else:
                print("\nNot valid input!\n\n Use:\n q w e \n a s d \n z x c \n to select your square\n")
                self.board.render()


    def play(self):
        while(True):
            #get where they want to play
            #attempt to place it on the board if successful move on
            position = self.get_input()

            if (self.board.set(position[0],position[1],1)):
                    return
            else:
                print("\nSquare already played! Select a new one!\n")
                self.board.render()
                

        
class AI:


    def __init__(self,board):
        self.board = board

    def play(self):
        while(True):
            play_position = (randint(0,2),randint(0,2))
            if (self.board.set(play_position[0],play_position[1],2)):
                    print("My move...\n")
                    return


        

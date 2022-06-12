"""
File Name: game.py

Author: Ntyam Adjomo Francky Ludovic

Purpose: Create a game called "Tic Tac Toe".
Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.

"""
from re import I
import click


def main():
    player = next_player("")
    board = create_board()
    while not (check_win(board) or draw_board(board)):
        print_board(board)
        move_player(player, board)
        player = next_player(player)
    print_board(board)
    print("Good game. Thanks for playing!") 
        
def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board
    
#create the function to display the board

def print_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
#create the function to check if the game is over
def draw_board(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
 
#create the function to do the comparison between the board and the player
def check_win(board):
    
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
    
    
# create the function that ask the input of the player
def  move_player(player, board):
      square = int(input(f"{player}'s turn to choose a square (1-9): "))
      board[square - 1] = player
    
 #create the function to help to go to the next player   
def next_player(current):
    if current == "" or current == "o":
       
        return "\033[34m" + "x" + "\033[0m"
    elif current == 'x':
        return "\033[34m" + "o" + "\033[0m"


if __name__ == "__main__":
    main()
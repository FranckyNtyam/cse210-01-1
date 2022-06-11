"""
File Name: pygame.py

Author: Ntyam Adjomo Francky Ludovic

Purpose: Create a pygame called "Tic Tac Toe".
Tic-Tac-Toe is a pygame in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.

"""
import pygame
import sys

# Initialize pygame
pygame.init()

#Create Window
WIDTH =500; HEIGHT = 500
ROWS = 20
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    def draw(width, cell_width,cell_height, surface, rows):
        x = 0 ; o = 0
       
        """
        Draw a grid of width x height.
        """
        for i in range(rows):
            x += cell_width
            o = cell_height
            pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
            pygame.draw.line(surface, (255, 255, 255, (0, o), (width, o)))
        
        while True:
            draw(WIDTH, HEIGHT/ROWS,WIDTH/ROWS, WINDOW, ROWS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            
main()
import pygame
import sys
from grid import Grid

pygame.init()
dark_blue = (0,0,128)


screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")
grid = Grid()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    #Drawing the background
    screen.fill(dark_blue)
  
    pygame.display.update()
    clock.tick(60)        


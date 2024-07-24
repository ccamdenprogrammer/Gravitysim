import pygame
pygame.init()
import math


WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Gravitysim")

def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    pygame.quit()
    
main()
            
    
    


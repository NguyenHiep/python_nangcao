import pygame		#1
import time		#4

pygame.init()		#2
gameDisplay = pygame.display.set_mode((800,600))	#3
pygame.display.set_caption("Name of the Game")		#3
clock = pygame.time.Clock() 	#4
crashed = False	#5
while not crashed:	#6
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
            
    pygame.display.update()
    clock.tick(60)

pygame.quit()		#7
quit()

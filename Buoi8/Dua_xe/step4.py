import pygame		#1
import time		#4

pygame.init()		#2

display_width = 800     #8
display_height = 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73 #19

gameDisplay = pygame.display.set_mode((display_width,display_height))	#3
pygame.display.set_caption("Racing car")    #3

clock = pygame.time.Clock() 	#4
#crashed = False #5
carImg = pygame.image.load('racecar1.png')   #9

def car(x,y):   #10
    gameDisplay.blit(carImg, (x,y))

def game_loop(): #20
    x =  (display_width * 0.45) #11
    y = (display_height * 0.8)

    x_change = 0    #14
    car_speed = 0

    gameExit = False
    
    while not gameExit:	#6
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True            
            if event.type == pygame.KEYDOWN:    #15
                if event.key == pygame.K_LEFT:  #16
                    x_change = -5   #17
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            
        x += x_change   #18
            
        gameDisplay.fill(white) #12
        car(x,y)    #13

        if x > display_width - car_width or x < 0:  #21
            gameExit = True

        pygame.display.update()
        clock.tick(60)

game_loop()     #22
pygame.quit()		#7
quit()

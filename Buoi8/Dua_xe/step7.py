import pygame		#1
import time		#4
import random

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

def text_objects(text, font):   #23
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):  #24
    largeText = pygame.font.Font('freesansbold.ttf',85)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def game_over():    #25
    message_display('Game over')

#######
def things(thingx, thingy, thingw, thingh, color):  #27
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
#######

def game_loop(): #20
    x =  (display_width * 0.45) #11
    y = (display_height * 0.8)

    x_change = 0    #14
    #car_speed = 0
    ######  #28
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    ######

    gameExit = False
    
    while not gameExit:	#6
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #gameExit = True
                pygame.quit()
                quit()
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
        
        ######  #29
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)    #13
        ######
        if x > display_width - car_width or x < 0:  #21
            #gameExit = True
            game_over() #26
            
        if thing_starty > display_height:   # 30
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
        ######
        if y < thing_starty+thing_height:   #31
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width\
                                or x+car_width > thing_startx\
                                and x + car_width < thing_startx+thing_width:
                print('x crossover')
                game_over()
        ######
        pygame.display.update()
        clock.tick(60)

game_loop()     #22
pygame.quit()	#7
quit()

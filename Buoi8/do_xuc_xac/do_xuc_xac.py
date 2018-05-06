import pygame		
from random import randint
import sys
import time

sys.setrecursionlimit(123456789)
	

pygame.init()		

display_width = 300     
display_height = 300
black = (0,0,0)
white = (255,255,255)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))	
pygame.display.set_caption("Dices-Playing")
clock = pygame.time.Clock()

gameIcon = pygame.image.load('sau.png') 
pygame.display.set_icon(gameIcon)

xuc_xac_1 = pygame.image.load('mot.png')
xuc_xac_2 = pygame.image.load('hai.png')
xuc_xac_3 = pygame.image.load('ba.png')
xuc_xac_4 = pygame.image.load('bon.png')
xuc_xac_5 = pygame.image.load('nam.png')
xuc_xac_6 = pygame.image.load('sau.png')

list_xuc_xac = []
list_xuc_xac.append(xuc_xac_1)
list_xuc_xac.append(xuc_xac_1)
list_xuc_xac.append(xuc_xac_2)
list_xuc_xac.append(xuc_xac_3)
list_xuc_xac.append(xuc_xac_4)
list_xuc_xac.append(xuc_xac_5)
list_xuc_xac.append(xuc_xac_6)


def ve_co(x,y,ten_co):   
    gameDisplay.blit(ten_co, (x,y))

x1 = (display_width/2) - 120 
y1 = (display_height/8)

x2 = (display_width/2) + 30
y2 = (display_height/8)

def text_objects(text, font):   
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    
    smallText = pygame.font.SysFont("comicsansms",16)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
    clock.tick(15) 

def quit_game():
     pygame.quit()
     quit()

def game_intro():
    intro = True    
    while intro:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                #intro = False
                pygame.quit()
                quit()                             
        gameDisplay.fill(white) 
        ve_co(x1,y1,xuc_xac_1)    
        ve_co(x2,y2,xuc_xac_1)    

        button("Play",x1+50,y2+120,150,50,green,bright_green, game_loop)
        button("Quit",x1+50,y2+180,150,50,red,bright_red,quit_game)
        pygame.display.update()
        clock.tick(15) 

def game_loop():
    so1 = randint(1, 6)
    so2 = randint(1, 6)
    gameExit = False
    while not gameExit:	
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #gameExit = True
                pygame.quit()		
                quit()            
        
        gameDisplay.fill(white) 
        ve_co(x1,y1,list_xuc_xac[so1])    
        ve_co(x2,y2,list_xuc_xac[so2])    

        button("Play",x1+50,y2+120,150,50,green,bright_green, game_loop)
        button("Quit",x1+50,y2+180,150,50,red,bright_red,quit_game)
        
        pygame.display.update()
        clock.tick(30) 

game_intro()
game_loop()
pygame.quit()		
quit()

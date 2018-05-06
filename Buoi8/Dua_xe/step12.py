import pygame		#1
import time		#4
import random

pygame.init()		#2

display_width = 800     #8
display_height = 600
black = (0,0,0)
white = (255,255,255)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
######  #38
bright_red = (255,0,0)
bright_green = (0,255,0)
######
car_width = 73 #19



gameDisplay = pygame.display.set_mode((display_width,display_height))	#3
pygame.display.set_caption("Racing car")    #3

clock = pygame.time.Clock() 	#4
#crashed = False #5
carImg = pygame.image.load('racecar1.png')   #9

gameIcon = pygame.image.load('carIcon.png') #47
pygame.display.set_icon(gameIcon)

pause = False #42

def car(x,y):   #10
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):   #23
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_over():    #25 
    #message_display('Game over')
    # Update game over # 46
    largeText = pygame.font.SysFont("comicsansms",90)
    TextSurf, TextRect = text_objects("Game over", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quit_game)

        pygame.display.update()
        clock.tick(15) 
    

def things(thingx, thingy, thingw, thingh, color):  #27
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

#32
def display_marks(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Marks: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

######  #39
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

#40
def quit_game():
     pygame.quit()
     quit()

###### #44
def unpause():
    global pause    
    pause = False
    print(pause)

######  #43
def paused():
    
    #gameDisplay.fill(white)
    '''
    largeText = pygame.font.SysFont("freesansbold.ttf",90)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    '''

    largeText = pygame.font.SysFont("comicsansms",90)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    print('Come hete!!!')
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quit_game)

        pygame.display.update()
        clock.tick(15)   


       
#36
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = text_objects("Start Game", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        ###### 41
        button("Start",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quit_game)
        ######
        pygame.display.update()
        clock.tick(15)

def game_loop(): #20
    global pause #45
    x =  (display_width * 0.45) #11
    y = (display_height * 0.8)

    x_change = 0    #14
    #car_speed = 0
    #28
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    ######  #33
    thingCount = 1
    dodged = 0
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
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:    #45                   
                    pause = True
                    paused()                  
                                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                
        x += x_change   #18            
        gameDisplay.fill(white) #12
        
        #29
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, blue)
        thing_starty += thing_speed
        car(x,y)    #13
        ###### #34
        display_marks(dodged)
        ######
        if x > display_width - car_width or x < 0:  #21
            #gameExit = True
            game_over() #26
            
        if thing_starty > display_height:   # 30
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            ###### #35
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
            ######
        if y < thing_starty+thing_height:   #31
            #print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width\
                                or x+car_width > thing_startx\
                                and x + car_width < thing_startx+thing_width:
                #print('x crossover')
                game_over()
        ######
        pygame.display.update()
        clock.tick(60)


game_intro()    #37
game_loop()     #22
pygame.quit()	#7
quit()

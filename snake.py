# Imports and starting pygame
import pygame 
import time 
import random 
pygame.init()

# Window and Colours Variables
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('GAMES')
White = (255,255,255)
Red = (255,0,0)
Black = (0,0,0)

# Dimensions of the playingfield
width = 100
height = 100

# Shape Variables
Rectangle1 = pygame.Rect(100,50,600,150)
Rectangle2 = pygame.Rect(300,250,200,75)
Rectangle3 = pygame.Rect(0,0,800,600)
Rectangle4 = pygame.Rect(190,90,410,410)
RectangleV = pygame.Rect(650,100,100,50)
RectangleD1 = pygame.Rect(50,50,700,150)
RectangleD2 = pygame.Rect(50,216,700,150)
RectangleD3 = pygame.Rect(50,382,700,150) 
RectangleQ1 = pygame.Rect(100,100,600,400)
RectangleQ2 = pygame.Rect(110,110,580,180)
RectangleQ3 = pygame.Rect(110,310,580,180)

# Snake position 
x1 = 395
y1 = 295
x1_change = 0
y1_change = 0

# Speed of snake 
clock = pygame.time.Clock()

# Snake length
snakecoor = []
snakel = 0

# Apple
applex = round(random.randrange(210, 590 - 10) / 10) * 10
appley = round(random.randrange(110, 490 - 10) / 10) * 10

# Font Variables
font1 = pygame.font.Font('freesansbold.ttf', 140)
font2 = pygame.font.Font('freesansbold.ttf', 60)
font3 = pygame.font.Font('freesansbold.ttf', 20)
fontg = pygame.font.Font('freesansbold.ttf', 120)
fontp = pygame.font.Font('freesansbold.ttf', 80)
fontq = pygame.font.Font('freesansbold.ttf', 100) 
fontv = pygame.font.Font('freesansbold.ttf', 20) 

# Diffulculty select Font Variables
fontd = pygame.font.Font('freesansbold.ttf', 120) 

# Text Variables
text1 = font1.render('SNAKE', True, White)
text2 = font2.render('PLAY', True, White)
text3 = font3.render('Created by Bekety Studios', True, White)
textg = fontg.render('GAME OVER', True, Red)
textq1 = fontq.render('Play again', True, White)
textq2 = fontq.render('Quit Game', True, White)

# Diffulculty select Text Variables
textd1 = fontd.render('Easy', True, White) 
textd2 = fontd.render('Medium', True, White) 
textd3 = fontd.render('Hard', True, White) 

# Text Rectangle Variables
Joe1 = text1.get_rect()
Joe2 = text2.get_rect()
Joe3 = text3.get_rect()
Joeg = textg.get_rect()
Joeq1 = textq1.get_rect() 
Joeq2 = textq2.get_rect()

# Diffulculty select Text Rectangle Variables
Joed1 = textd1.get_rect()
Joed2 = textd2.get_rect()
Joed3 = textd3.get_rect()

# Functions
def assign_pixel(pf,w,h,type):
    pf[w][h] = type
def apple(pf):
    success = False 
    while success == False:
        x = random.randint(0,99)
        y = random.randint(0,99)
        if pf[x][y] == 0:
            assign_pixel(pf,x,y,9)
            success = True
            print(x, y) 
        else:
            success = False 
def duplicate_check(snakecoor):
    if len(snakecoor) == len(set(snakecoor)):
        return False
    else:
        return True
def points_show(points):
    value = fontp.render("Points: " + str(points), True, White)
    window.blit(value, [220, 0])

# Snake Game
def WHOLES():
    # Clear screen 
    pygame.draw.rect(window,Black,Rectangle3)
    pygame.display.flip()

    # Design for diffuculty select (Rectangle)
    pygame.draw.rect(window,White,RectangleD1,8) 
    pygame.display.flip()
    pygame.draw.rect(window,White,RectangleD2,8) 
    pygame.display.flip()
    pygame.draw.rect(window,White,RectangleD3,8) 
    pygame.display.flip()

    # Design for diffuculty select (Text)
    Joed1.center = (400,125)
    window.blit(textd1, Joed1)
    pygame.display.update() 
    Joed2.center = (400,291)
    window.blit(textd2, Joed2)
    pygame.display.update() 
    Joed3.center = (400,475)
    window.blit(textd3, Joed3)
    pygame.display.update() 

    # Selecting diffulculty
    sspeed = 0
    pressed = False 
    while pressed == False:
        for event in pygame.event.get():
             if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx >= 50 and mx <= 750 and my >= 50 and my <= 200:
                    pygame.draw.rect(window,Red,RectangleD1)
                    pygame.display.flip()
                    window.blit(textd1, Joed1)
                    pygame.display.update()
                    pressed = True 
                    sspeed = 10
                elif mx >= 50 and mx <= 750 and my >= 216 and my <= 366:
                    pygame.draw.rect(window,Red,RectangleD2)
                    pygame.display.flip()
                    window.blit(textd2, Joed2)
                    pygame.display.update()
                    pressed = True 
                    sspeed = 30
                elif mx >= 50 and mx <= 750 and my >= 382 and my <= 532: 
                    pygame.draw.rect(window,Red,RectangleD3)
                    pygame.display.flip()
                    window.blit(textd3, Joed3)
                    pygame.display.update()
                    pressed = True 
                    sspeed = 50
                else:
                    pressed = False 

    time.sleep(0.1)

    # Clear screen
    pygame.draw.rect(window,Black,Rectangle3)
    pygame.display.flip()

    # Playing area
    pygame.draw.rect(window,White,Rectangle4,10)
    pygame.display.flip()

    # Controlling the snake
    def Snake_Game():
        x1 = 400
        y1 = 300
        x1_change = 0
        y1_change = 0
        applex = round(random.randrange(210, 590 - 10) / 10.0) * 10.0
        appley = round(random.randrange(110, 490 - 10) / 10.0) * 10.0
        snakel = 0
        GO = False
        Moving = False

        while not GO: 
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -10
                            y1_change = 0
                            Moving = True
                        elif event.key == pygame.K_RIGHT:
                            x1_change = 10
                            y1_change = 0
                            Moving = True
                        elif event.key == pygame.K_UP:
                            y1_change = -10 
                            x1_change = 0
                            Moving = True
                        elif event.key == pygame.K_DOWN:
                            y1_change = 10
                            x1_change = 0
                            Moving = True

            x1 += x1_change
            y1 += y1_change 

            # Boundraies 
            if x1 >= 590 or x1 <= 195 or y1 >= 490 or y1 <= 95:
                GO = True

            # Eating apples and checking if you are in inside of yourself
            apple_eaten = False
    
            snakecoor.append((x1, y1))

            dc = duplicate_check(snakecoor)

            if dc and Moving:
                GO = True  

            if x1 == applex and y1 == appley:
               applex = round(random.randrange(210, 590 - 10) / 10.0) * 10.0
               appley = round(random.randrange(110, 490 - 10) / 10.0) * 10.0
               snakel += 1
               apple_eaten = True

            # Redrawing the area
            pygame.draw.rect(window,Black,Rectangle3)
            pygame.draw.rect(window,White,Rectangle4,10)
            pygame.draw.rect(window,Red,[applex, appley, 10 ,10])
            points_show(snakel)
            pygame.display.flip()
    
            # The shape of the snake
            for i in snakecoor:
                pygame.draw.rect(window, White, [i[0], i[1], 10, 10])
            pygame.display.update()

            if apple_eaten == False:
                snakecoor.pop(0)        

            # Game over screen
            if GO == True: 
                pygame.draw.rect(window,Black,Rectangle3) 
                pygame.display.flip()
                Joeg.center = (400, 300)
                window.blit(textg, Joeg)
                pygame.display.update()
                snakecoor.clear()
                time.sleep(1)
    
            # Speed of snake
            clock.tick(sspeed)

    # Printing the play again and quit screen
    finish = False

    while finish == False:
        Snake_Game()
        pygame.draw.rect(window,Black,Rectangle3)
        pygame.draw.rect(window,White,RectangleQ1,6)
        pygame.draw.rect(window,White,RectangleQ2,4)
        pygame.draw.rect(window,White,RectangleQ3,4)
        Joeq1.center = (400,200)
        window.blit(textq1, Joeq1)
        Joeq2.center = (400,400)
        window.blit(textq2, Joeq2)
        pygame.display.update() 

        play_again = False 

        while play_again == False:           
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mx >= 110 and mx <= 690 and my >= 110 and my <= 290:
                        pygame.draw.rect(window,Red,RectangleQ2)
                        pygame.display.flip()
                        window.blit(textq1, Joeq1)
                        pygame.display.update()
                        time.sleep(0.1)
                        play_again = True
                    elif mx >= 110 and mx <= 690 and my >= 310 and my <= 490:
                        pygame.draw.rect(window,Red,RectangleQ3)
                        pygame.display.flip()
                        window.blit(textq2, Joeq2)
                        pygame.display.update()
                        play_again = True
                        finish = True

# Music 
pygame.mixer.music.load('2-16. Price.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.07)

# Design of Title screen (Rectangles)
pygame.draw.rect(window,White,Rectangle1,8)
pygame.draw.rect(window,White,Rectangle2,8) 
pygame.display.flip()

# 13: Design of Title screen (Text)
Joe1.center = (400,125)
window.blit(text1, Joe1)
Joe2.center = (400,287.5)
window.blit(text2, Joe2)
Joe3.center = (650,550)
window.blit(text3, Joe3)
pygame.display.update() 

# Clicking play
mppressed = False
while mppressed == False:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx >= 300 and mx <= 500 and my >= 250 and my <= 325:
                pygame.draw.rect(window,Red,Rectangle2)
                window.blit(text2, Joe2)
                pygame.display.update()
                time.sleep(0.1)
                mppressed = True
                WHOLES()
        else:
           mppressed = False
pygame.quit()
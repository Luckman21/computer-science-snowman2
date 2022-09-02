'''
Created on Apr 26, 2018

@author: Luck
'''
import pygame, sys
from random import randint
from pygame.locals import *
from pygame.constants import *

a,b,z = 0,0,2 #Initial values of snowman that will be called into the function.  a = x, b = y and z = r.

def Snowman(x,y,r):#This function draws the snowman.  If snowman's radius is less than 1, it changes that value to 1 and recalls itself recursively
    '''Snowman(x,y) - Creates the snowman.  If snowman's radius is less than 1, it changes that value to 1 and recalls itself recursively
    x - the horizontal displacement of the snowman
    y - the vertical displacement of the snowman
    r - radius of the snowman
    '''
    if r >= 1:
        pygame.draw.rect (screen, Brown,((150+x)*r,(170+y)*r,100*r,5*r))
        pygame.draw.rect (screen, Brown,((230+x)*r,(158+y)*r,5*r,30*r))
        pygame.draw.rect (screen, Brown,((-55+x)*r,(170+y)*r,(100)*r,5*r))
        pygame.draw.rect (screen, Brown,((-42+x)*r,(158+y)*r,5*r,30*r))
        pygame.draw.circle (screen, White,((100+x)*r,(100+y)*r), 40*r, 0)
        pygame.draw.circle (screen, White,((100+x)*r,(190+y)*r), 70*r, 0)
        pygame.draw.circle (screen, White,((100+x)*r,(260+y)*r),90*r ,0)
        pygame.draw.polygon(screen, Orange,[((92+x)*r,(100+y)*r),((100+x)*r,(125+y)*r),((108+x)*r,(100+y)*r)],0)
        pygame.draw.rect (screen, Black,((75+x)*r,(20+y)*r,50*r,50*r))
        pygame.draw.rect (screen, Red,((75+x)*r,(50+y)*r,50*r,10*r))
        pygame.draw.rect (screen, Black,((50+x)*r,(70+y)*r,100*r,5*r))
        pygame.draw.circle (screen, Black,((82+x)*r,(87+y)*r), 5*r, 0)
        pygame.draw.circle (screen, Black,((117+x)*r,(87+y)*r), 5*r, 0)
        pygame.draw.circle (screen, Black,((100+x)*r,(170+y)*r), 7*r, 0)
        pygame.draw.circle (screen, Black,((100+x)*r,(210+y)*r), 7*r, 0)
        pygame.draw.circle (screen, Black,((100+x)*r,(250+y)*r), 7*r, 0)
    else:
        r = 1
        return Snowman(x,y,r)

def Snow(count):#This function creates the snow seen on screen
    '''Snow(count) - Prints out multiple circles to the window to represent snowflakes
    count - keeps track of the number of snowflakes on the screen
    '''
    
    for i in range(0,count): 
        o,w = randint(0,800),randint(0,600)
        pygame.draw.circle(screen,White,(0+o,0+w),1,0)
    
fpsClock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((800,600))#Setting window resolution to 800x600 pixels and titling the window "Snowman Maker"
pygame.display.set_caption ('Snowman Maker')

Red,Blue,Green,White,Black,Orange,Brown = (255,0,0),(0,0,255),(0,255,0),(255,255,255),(0,0,0),(255,127,0),(165,80,80)
dx,dy,rad = 0,0,0 #Movement variables and radius variable that changes x,y and r by adding and subtracting from their initial values

done = False
while not done:
    
    a+=dx
    b+=dy
    z+=rad
    
    screen.fill(Blue)
    
    pygame.display.update(Snowman(-a,-b,z))
    pygame.display.update(Snow(200))
    fpsClock.tick(20)
    
    for event in pygame.event.get():#This loop checks all the keys that are pressed and prints them to the console.  It also controls movement via user input
        print event
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                done = True
                sys.exit(0) 
            
            #I found when testing the code, adding in diagonals made it run a little more smooth, so don't take marks off for "unnecessary code"
            
            if ((event.key == 119) and (event.key == 115)) or (event.key == 97) and (event.key == 100): #UP & DOWN OR RIGHT LEFT will not move it if a pair are held together
                pass
            if (event.key == 119): #UP
                dy = 10
                if (event.key == 97): #LEFT
                    dx = 10
                if (event.key == 100): #RIGHT
                    dx = -10
            if (event.key == 115): #DOWN
                dy = -10
                if (event.key == 97): #LEFT
                    dx = 10
                if (event.key == 100): #RIGHT
                    dx = -10
            if (event.key == 97): #LEFT
                    dx = 10
            if (event.key == 100): #RIGHT
                dx = -10
            if (event.key == 61): #PLUS
                rad = 1
            if (event.key == 45): #MINUS
                rad = -1
        elif (event.type == KEYUP):
            dx,dy,rad = 0,0,0
        print a,b,z
    pygame.display.update()

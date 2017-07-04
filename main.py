import pygame
import math
from pygame.locals import *
import random


#global variables
 
global background, game_running, game, white, global_counter, gameclock, asteroid_timer

pygame.mixer.init()

#load the images
background = pygame.image.load("images/background.png")
ship = pygame.image.load("images/ship.png")
pause = pygame.image.load("images/pause.png")
laser1 = pygame.image.load("images/laser.png")
laser2 = pygame.image.load("images/laser2.png")
laser3 = pygame.image.load("images/laser3.png")
upgraded_laser = pygame.image.load("images/bluelaser.png")

score1 = pygame.image.load("images/score.png")
earth = pygame.image.load("images/earth.png")
ufo1 = pygame.image.load("images/ufo1.png")
ufo2 = pygame.image.load("images/ufo2.png")
ufo3 = pygame.image.load("images/ufo3.png")
hit =  pygame.image.load("images/explosion.png")
lasercannon = pygame.image.load("images/lasercannon.png")
laserupgrade = pygame.image.load("images/laserupgrade.png")

upgradedict = {1: lasercannon, 2: laserupgrade}


#music

shoot = pygame.mixer.Sound("music/shoot.wav")
hit2 =pygame.mixer.Sound("music/explode.wav")
powerupsound = pygame.mixer.Sound("music/powerupsound.wav")
powerupsound.set_volume(0.02)                            
shoot.set_volume(0.03)
hit2.set_volume(0.03)
soundtrack = pygame.mixer.Sound("music/Cosmic Messages.wav")
pygame.mixer.music.load("music/Cosmic Messages.wav")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.1)
                 

game_running = True # initialise the game
red = (255,0,0)
white = (255,255,255)
gameclock = pygame.time.Clock()


asteroid_health_dict = {1: 3, 2: 5, 3: 7}
asteroid_dict =  {1: ufo1, 2: ufo2, 3:ufo3}


def game_start():
    game_running = True



def play_again(): #restart the game and reini55tialise all the globals in the inner loop
    text = font.render('Game Over, Press any key to play again.', 13, white)
    textx = 599 / 2 - text.get_width() / 2
    texty = 800 / 2 - text.get_height() / 2
    textx_size = text.get_width()
    texty_size = text.get_height()
##    pygame.draw.rect(screen, (255, 255, 255), ((textx - 5, texty - 5),
##                                               (textx_size + 10, texty_size +
##                                                10)))

    screen.blit(text, (152,394))

    pygame.display.flip()
    playing_again = True
    while playing_again:
        gameclock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing_again = False
                pygame.display.quit()
                pygame.quit()
                quit()
##            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
##                x, y = event.pos
##                if x >= textx - 5 and x <= textx + textx_size + 5:
##                    if y >= texty - 5 and y <= texty + texty_size + 5:
##                        playing_again = False
##                        break
 
            elif event.type == pygame.KEYDOWN:
                playing_again = False

    



def main_menu():   #initialise the start of the game, a UI interface for starting the game!
    in_main_menu  = 1

def pause_menu(): #pause menu for when the escape key is pressed
    pause_menu = 1
    while pause_menu == 1:
         pygame.mixer.music.pause()
         screen.blit(pause, (65, 175))
         pygame.display.flip()
         for event in pygame.event.get():
             
             if event.type == pygame.QUIT:
                game = False
                pygame.display.quit()
                pygame.quit()
                quit()
             elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                     pause_menu = 0
    pygame.mixer.music.unpause()

game_start()
while game_running :
    gameclock.tick(50) #set fps to 50
    pygame.init()
    pygame.display.init()
    pygame.mixer.init()
    screen= pygame.display.set_mode((599,800))
    pygame.mixer.init() # start music
    global_counter = 0
    shippos = [275, 725]
    shipmoving = [False,False,False,False]
    asteroids = []    # asteroids have 4characteristics-> [[posx, posy], type, health, initialised]
    lasers = [] # lasers have 2 characters -> [[posx,posy], direction] 
    shippos1 = shippos
    score = 0
    asteroid_timer = 0
    earth_health = 100
    win_status = False
    game = True
    powerups = []
    poweruptimer = 0 
    laser_cannon_level = 0     #triple lasers
    laser_damage_upgrade = 0   #powerup number 2
    poweruplasts = 250
    have_powerup = False
    text_timer = 0
    font= pygame.font.Font(None,24)
    
    while game:
        global_counter+= 1 #set scrolling background
        asteroid_timer += 1 #timer interval for asteroids to spawn
        poweruptimer +=1# timer for powerups spawningda
      
                
        screen.fill(white)
        screen.blit(background, [0, (global_counter%800)])
        screen.blit(background, (0,-800+(global_counter % 800)))
##        screen.blit(earth, (0,550))
        screen.blit(ship, shippos)
        screen.blit(score1, (0, 0))
        pygame.display.flip()
    
        health = font.render("Health:" + str(earth_health), 13, red)
        screen.blit(health, (500,17))
        #timer for the powerup to be temporary
        if have_powerup == True:
            if laser_cannon_level == 1:
                text = font.render("Triple Laser Cannon Obtained! Losing Powerup in:" + str(((poweruplasts)/50)), 13, red)
            else:
                text = font.render("Double Damage Laser Obtained! Losing Powerup in:" + str(((poweruplasts)/50)), 13, red)
            screen.blit(text, (102,394) )
            poweruplasts -= 1
            if poweruplasts == 0:
                have_powerup = False
                laser_cannon_level = 0
                laser_damage_uprade = 0
                poweruplasts = 250
        

                
        #randomly spawn asteroids
        timer2 = 0
        if asteroid_timer == 100:
            asteroids.append([[random.randint(20, 500), 0], random.randint(1, 3), 0, 0])
            asteroid_timer = timer2*2
            if timer2 <= 40:
                timer2+= 3
        
        #randomly spawn powerups
        if poweruptimer == 100:
            powerups.append([[random.randint(20, 500), 0], random.randint(1,2)])
            poweruptimer = 0
            
        #queue the powerups and activate the powerups
        powerupcounter = 0
        for powerup in powerups:
            powerupspeed = 5
            powerup[0][1] += 5
            poweruprect = pygame.Rect(laser1.get_rect())
            poweruprect.top = powerup[0][0]
            poweruprect.left = powerup[0][1]
            shiprect = pygame.Rect(laser1.get_rect())
            shiprect.top = shippos[0]
            shiprect.left = shippos[1]
            
            if powerup[1] == 1:
                screen.blit(lasercannon, powerup[0])
            elif powerup[1] == 2:
                screen.blit(laserupgrade, powerup[0])
                
            if shiprect.colliderect(poweruprect):
                powerups.pop(powerupcounter)
                have_powerup = True
                poweruplasts = 250
                if powerup[1] == 1:
                    laser_cannon_level = 1
                    laser_damage_upgrade = 0
                    powerupsound.play()
                elif powerup[1] == 2:
                    laser_damage_upgrade = 1
                    laser_cannon_level = 0
                    powerupsound.play()
                    
            powerupcounter += 1
                    
                


        #collisions of asteroids
        asteroid_counter = 0
        for asteroid in asteroids:
            
            if asteroid[3] == 0:              
                asteroid[2] = asteroid_health_dict[asteroid[1]]
                asteroid[3] = 1
                
            asteroidspeed = asteroid[1] * 2
            asteroid[0][1] += asteroidspeed
            asteroidrect = pygame.Rect(asteroid_dict[asteroid[1]].get_rect())
            asteroidrect.top = asteroid[0][1]
            asteroidrect.left = asteroid[0][0] 

        #asteroids hitting earth
            
            if asteroidrect.top >= 800:
                earth_health -= asteroid[1]*(random.randint(5,10))
                asteroids.pop(asteroid_counter)
                
            
            pygame.display.flip()
            laserindex = 0

            #collisions with asteroids and lasers
            
            for laser in lasers:
                laserrect = pygame.Rect(laser1.get_rect())
                laserrect.top = laser[0][1]
                laserrect.left = laser[0][0]
                asteroidrect = pygame.Rect(asteroid_dict[asteroid[1]].get_rect())
                asteroidrect.top = asteroid[0][1]
                asteroidrect.left = asteroid[0][0]
                if asteroidrect.colliderect(laserrect):
                    screen.blit(hit, (laser[0][0], laser[0][1]-25))
                    hit2.play()
                    lasers.pop(laserindex)
                    if laser_damage_upgrade == 0:     
                          asteroid[2] -= 1
                    else:
                        asteroid[2] -= 2
                    if asteroid[2] <= 0:
                            score += asteroid[1]*2
                            asteroids.pop(asteroid_counter)
                        
                laserindex += 1
            asteroid_counter += 1
        for asteroid in asteroids:
            screen.blit(asteroid_dict[asteroid[1]], asteroid[0])

        #show current Score
        font= pygame.font.Font(None,24)
        scoretext = font.render(str(score), True, white)
        textRect= scoretext.get_rect()
        textRect.topright = [118,19]
        screen.blit(scoretext, textRect)
        

            
        #show the lasers
        laserindex = 0    
        for laser in lasers:
                   
                    laserspeed = 10
                    if laser[0][1] <= 0 or laser[0][0] <= 0 or laser[0][0] >= 600:
                        lasers.pop(laserindex)
                        
                    if laser[1] == 0:
                        laser[0][1] -= laserspeed
                        if laser_damage_upgrade==0:
                            screen.blit(laser1, (laser[0][0]+25, laser[0][1]))
                        else:
                            screen.blit(upgraded_laser, (laser[0][0]+25, laser[0][1]))
                    else:
                        laser[0][1] -= laserspeed*math.sin(math.pi/3)
                        laser[0][0] -= laserspeed*math.cos(math.pi/3)* laser[1]
                        if laser[1] == 1:
                            screen.blit(laser2, (laser[0][0]+25, laser[0][1]))
                        else:
                            screen.blit(laser3, (laser[0][0]+25, laser[0][1]))
                    laserindex += 1
                    
             
                    
        #loop through actions in keyboard
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                play_again()
                game = False
                exit(0)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                   
                    pause_menu()
                elif event.key == pygame.K_r:
                    game = False 
                elif event.key == pygame.K_SPACE:
                    position = pygame.mouse.get_pos()
                    lasers.append([[shippos[0], shippos[1]], 0])
                    if laser_cannon_level == 1:
                        lasers.append([[shippos[0], shippos[1]], -1])
                        lasers.append([[shippos[0], shippos[1]], 1])
                        shoot.play()
                    shoot.play()
                elif event.key==pygame.K_w:
                    shipmoving[0]=True
                elif event.key==pygame.K_a:
                    shipmoving[1]=True
                elif event.key==pygame.K_s:
                    shipmoving[2]=True
                elif event.key==pygame.K_d:
                    shipmoving[3]=True
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                    shipmoving[0]=False
                elif event.key==pygame.K_a:
                    shipmoving[1]=False
                elif event.key==pygame.K_s:
                    shipmoving[2]=False
                elif event.key==pygame.K_d:
                    shipmoving[3]=False
                    

        if shippos[1] >= 670:
    
            if shipmoving[0]:
                shippos[1] -= 9
        if shippos[1] <= 725:
            if shipmoving[2]:
                shippos[1]+=9
        if shippos[0] >= 25:
            if shipmoving[1]:
                shippos[0]-=9
        if shippos[0] <= 525:
            if shipmoving[3]:
                shippos[0]+=9



        if earth_health <= 0:
            game = False
            win_status = False
            play_again()
            
        pygame.display.flip()







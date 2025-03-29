import pygame
import sys
import random
from tkinter import messagebox

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dice Roll Simulator")
rolling = False
pygame.display.update()
is_muted = False

# Loading images

main_background_image = pygame.image.load("Images/mainbg.png.jfif")
home_bt = pygame.image.load("Images/home_bt.png")
main_image = pygame.image.load("Images/rolldice.png")
roll_background_image = pygame.image.load("Images/th.jpg")
predict_img = pygame.image.load("Images/PREDICT.png")
roll_bt_img= pygame.image.load("Images/roll.png")
starting_dice_image = pygame.image.load("Images/1.png")
dice_2 = pygame.image.load("images/rolling-dices.png")
home_button = pygame.image.load("Images/home.jfif")
on = pygame.image.load("Images/volume-up.png")
off = pygame.image.load("Images/volume-off.png")
transparent = pygame.image.load("Images/trans.jpg")
roll_button_img =pygame.image.load("Images/roll_button.png")
dice_img_1 = pygame.image.load("rolling_img/1.png")
dice_img_2 = pygame.image.load("rolling_img/2.png")
dice_img_3 = pygame.image.load("rolling_img/3.png")
dice_img_4 = pygame.image.load("rolling_img/4.png")
dice_img_5 = pygame.image.load("rolling_img/5.png")
dice_img_6 = pygame.image.load("rolling_img/6.png")
pause = pygame.image.load("Images/pause.png")
resume = pygame.image.load("Images/resume.png")
# Loading audio

rolling_aud = pygame.mixer.Sound('Audio/roll_aud.mp3')
rolling_stp_aud = pygame.mixer.Sound('Audio/roll_stop.mp3')
click = pygame.mixer.Sound("Audio/mouse-click.mp3")
click.set_volume(0.07)

# To get the area of the button  

def button(x,y,image):
    width = image.get_width()
    height = image.get_height()
    return pygame.Rect(x,y,width,height)

########################################################

############################################
def resumemenu1():
    global is_muted
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
            screen.blit(transparent,(0,0))
            screen.blit(resume, (750,0))
            res=button(750,0,resume)
            screen.blit(home_button,(290,350))
            if is_muted == False:
                screen.blit(on, (290,250 ))
            else:
                screen.blit(off, (290,250 ))
            pos = pygame.mouse.get_pos()
            pygame.display.update()
            home = button(290,350,home_button)
            onn = button(290,250,on)
            if event.type == pygame.MOUSEBUTTONDOWN :
                if res.collidepoint(pos):
                    click.play()
                    roll()
                if home.collidepoint(pos):
                    click.play()
                    a=messagebox.askyesno(title="return to main menu",message="return to main menu")
                    if a == True:
                        main_page()
                    else:
                        break
                if onn.collidepoint(pos) and is_muted == False:
                    is_muted = True 
                    if is_muted:  
                         screen.blit(off, (290,250 ))
                         pygame.display.update()
                else  :
                         pos = pygame.mouse.get_pos() 
                         off_area = button(290,250,on)
                         if off_area.collidepoint(pos):
                             is_muted = False
                             click.play()
                             if  is_muted == False:
                                 screen.blit(on, (290,250))
                                 pygame.display.update()


##########################################
def resumemenu2():
    global is_muted
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
            screen.blit(transparent,(0,0))
            screen.blit(resume, (750,0))
            res=button(750,0,resume)
            screen.blit(home_button,(290,350))
            if is_muted == False:
                screen.blit(on, (290,250 ))
            else:
                screen.blit(off, (290,250 ))
            pos = pygame.mouse.get_pos()
            pygame.display.update()
            home = button(290,350,home_button)
            onn = button(290,250,on)
            if event.type == pygame.MOUSEBUTTONDOWN :
                if res.collidepoint(pos):
                    click.play()
                    roll2()
                if home.collidepoint(pos):
                    click.play()
                    a=messagebox.askyesno(title="return to main menu",message="return to main menu")
                    if a == True:
                        main_page()
                    else:
                        break
                if onn.collidepoint(pos) and is_muted == False:
                    is_muted = True 
                    if is_muted:  
                         screen.blit(off, (290,250 ))
                         pygame.display.update()
                else  :
                         pos = pygame.mouse.get_pos() 
                         off_area = button(290,250,on)
                         if off_area.collidepoint(pos):
                             is_muted = False
                             click.play()
                             if  is_muted == False:
                                 screen.blit(on, (290,250))
                                 pygame.display.update()
##########################################################
def roll_menu():
    global is_muted
    screen.blit(roll_background_image, (0, 0))
    screen.blit(home_bt, (750,0))
    pygame.display.update()
    while True:
        screen.blit(starting_dice_image, (150,350 ))
        screen.blit(dice_2, (450,350 ))
        pygame.display.update()
        for event in pygame.event.get():
            # To close the screen
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
            # return to main page
            if event.type == pygame.MOUSEBUTTONDOWN  : 
                pos = pygame.mouse.get_pos()
                home= button(750,0,home_bt)
                if home.collidepoint(pos):
                    click.play()
                    main_page()
                
            #to select how many dice (1 dice or 2 dice) to roll
            if event.type == pygame.MOUSEBUTTONDOWN : 
                pos = pygame.mouse.get_pos() 
                game_button = button(450,350,starting_dice_image)
                roll_button = button(150,350,dice_2)
                if roll_button.collidepoint(pos):
                    click.play()
                    roll()
                if game_button.collidepoint(pos):
                    click.play()
                    roll2()
########################################################
def roll2():
    global rolling
    global is_muted
    screen.blit(roll_background_image, (0, 0))
    screen.blit(starting_dice_image, (150,200 ))
    screen.blit(starting_dice_image, (450,200 ))
    screen.blit(roll_button_img, (350,450 ))
    screen.blit(pause, (750,0 ))
    pygame.display.update()
    while True:
        dice_rolling=[dice_img_1,dice_img_2,dice_img_3,dice_img_4,dice_img_5,dice_img_6]
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
            #To mute the audio
            if event.type == pygame.MOUSEBUTTONDOWN  :
                pos = pygame.mouse.get_pos()
                pause_area= button(750,0,pause)
                if pause_area.collidepoint(pos) :
                    click.play()
                    resumemenu2()
            # To check wheater the roll button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and rolling == False :
                pos = pygame.mouse.get_pos() 
                roll_button = button(350,450,roll_button_img)
                if roll_button.collidepoint(pos) and rolling == False: # check wheater the button is clicked and dice is not rolling
                    click.play()
                    rolling = True # to start the dice rolling
        # Print the rolling of dice 
        if rolling ==True  :  
                    pygame.time.delay(300)
                    if is_muted == False:
                        rolling_aud.play()
                    for i in range(6):
                        screen.blit(dice_rolling[i], (150,200 ))
                        screen.blit(dice_rolling[i], (450,200 ))
                        pygame.time.wait(250)
                        pygame.display.update()
                    global rand_img2
                    rand_img1=random.randint(1,6)
                    rand_img2=random.randint(1,6)
                    if rand_img1 == rand_img2 :
                        rand_img2 = random.randint(1,6)
                    if is_muted == False:
                        rolling_stp_aud.play()
                    final_dice_img1 = pygame.image.load("Images/"+str(rand_img1)+".png")
                    final_dice_img2 = pygame.image.load("Images/"+str(rand_img2)+".png")
                    screen.blit(final_dice_img1, (150,200 ))
                    screen.blit(final_dice_img2, (450,200 ))
                    pygame.event.clear()
                    rolling = False
                    pygame.display.update()
        pygame.display.update()
########################################################
# Code for rolling a dice

def roll():
    global rolling
    global is_muted
    screen.blit(roll_background_image, (0, 0))
    screen.blit(starting_dice_image, (280,200 ))
    screen.blit(roll_button_img, (350,450 ))
    screen.blit(pause, (750,0 ))
    pygame.display.update()
    while True:
        dice_rolling=[dice_img_1,dice_img_2,dice_img_3,dice_img_4,dice_img_5,dice_img_6]
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
            #To mute the audio
            if event.type == pygame.MOUSEBUTTONDOWN  :
                pos = pygame.mouse.get_pos()
                pause_area= button(750,0,pause)
                if pause_area.collidepoint(pos) :
                    click.play()
                    resumemenu1()
            # To check wheater the roll button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and rolling == False :
                pos = pygame.mouse.get_pos() 
                roll_button = button(350,450,roll_button_img)
                if roll_button.collidepoint(pos) and rolling == False: # check wheater the button is clicked and dice is not rolling
                    click.play()
                    rolling = True # to start the dice rolling
        # Print the rolling of dice
        if rolling ==True  :  
                    pygame.time.delay(300)
                    if is_muted == False:
                        rolling_aud.play()
                    for i in range(6):
                        screen.blit(dice_rolling[i], (280,200 ))
                        pygame.time.wait(250)
                        pygame.display.update()
                    rand_img=random.randint(1,6)
                    if is_muted == False:
                        rolling_stp_aud.play()
                    final_dice_img = pygame.image.load("Images/"+str(rand_img)+".png")
                    screen.blit(final_dice_img, (280,200 ))
                    pygame.event.clear()
                    rolling = False
                    pygame.display.update()
        pygame.display.update()
###################################################
def main_page():
    while True:
        screen.blit(main_background_image,(0,0))
        screen.blit(main_image,(310,60))
        screen.blit(roll_bt_img, (300,450 ))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # to quit the program
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN : # to check a mouse button is pressed
                pos = pygame.mouse.get_pos() # gets the mouse position
                roll_button = button(300,450,roll_bt_img)
                if roll_button.collidepoint(pos):
                    click.play()
                    roll_menu()
#####################################################
main_page()
pygame.display.update()

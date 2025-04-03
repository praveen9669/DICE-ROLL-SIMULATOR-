import pygame
import sys
import random
from tkinter import messagebox
import time

#Initialze

pygame.init()
pygame.mixer.init()
screen =pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dice Roll Simulator")
rolling = False
is_muted = False
WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
FONT = pygame.font.Font(None, 36)

# Loading images

main_background_image = pygame.image.load("Images/mainbg.jfif")
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
dice_img_1 = pygame.image.load("Images/1.png")
dice_img_2 = pygame.image.load("Images/2.png")
dice_img_3 = pygame.image.load("Images/3.png")
dice_img_4 = pygame.image.load("Images/4.png")
dice_img_5 = pygame.image.load("Images/5.png")
dice_img_6 = pygame.image.load("Images/6.png")
roll1 = pygame.image.load("Images/roll1.png")
roll2 = pygame.image.load("Images/roll2.png")
roll3 = pygame.image.load("Images/roll3.png")
roll4 = pygame.image.load("Images/roll4.png")
roll5 = pygame.image.load("Images/roll5.png")
roll6 = pygame.image.load("Images/roll6.png")
roll7 = pygame.image.load("Images/roll7.png")
roll8 = pygame.image.load("Images/roll8.png")
pause = pygame.image.load("Images/pause.png")
resume = pygame.image.load("Images/resume.png")

# Loading audio

rolling_aud = pygame.mixer.Sound('Audio/roll_aud.mp3')
won = pygame.mixer.Sound('Audio/won.mp3')
lost = pygame.mixer.Sound('Audio/lost.mp3')
rolling_stp_aud = pygame.mixer.Sound('Audio/roll_stop.mp3')
click = pygame.mixer.Sound("Audio/mouse-click.mp3")
click.set_volume(0.05)
lost.set_volume(0.07)

def resumemenu3():
    global is_muted
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
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
                    game_loop()
                if home.collidepoint(pos):
                    click.play()
                    a=messagebox.askyesno(title="HOME PAGE",message="Press 'YES' to return to Home")
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



def draw_text(text, x, y, size=10, color=WHITE):
    """ Draw text on the screen with a specified font size and color. """
    if isinstance(size, tuple):  
        size = size[0]  # Ensure 'size' is an integer
    
    font = pygame.font.Font(None, int(size))  # Convert size to integer if needed
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def roll_dice(predicted_number):
    temp_number = random.randint(1, 6)  # This is the final dice number
    dice_rolling = [
        pygame.image.load("Images/roll1.png"),
        pygame.image.load("Images/roll2.png"),
        pygame.image.load("Images/roll3.png"),
        pygame.image.load("Images/roll4.png"),
        pygame.image.load("Images/roll5.png"),
        pygame.image.load("Images/roll6.png"),
        pygame.image.load("Images/roll7.png"),
        pygame.image.load("Images/roll8.png")
    ]
    # Play rolling sound
    if is_muted == False:
        rolling_aud.play()
    roll_time = time.time() + 1.5  # Roll animation for 1.5 seconds
    while time.time() < roll_time:
        screen.blit(roll_background_image, (0, 0))

        # Ensure the animation is consistent with the final result
        random_face = random.randint(1, 6)  # Pick a number 1-6 to animate
        screen.blit(dice_rolling[random_face - 1], (300,180))

        pygame.display.flip()
        pygame.time.delay(100)
        pygame.event.pump()  # Prevent freezing

    # Stop rolling sound

    # Show the final dice result (Corrected to match temp_number)
    screen.blit(roll_background_image, (0, 0))
    f=pygame.image.load("Images/"+str(temp_number)+".png")
    screen.blit(f, (280,160))

    # Show result message
    if predicted_number == temp_number:
        result_text = "Correct Prediction!"
        pygame.time.wait(100)
        won.play()
        COL=GREEN
    else:
        result_text = "Wrong Prediction!"
        pygame.time.wait(100)
        lost.play()
        COL=RED
    draw_text(f"Rolled: {temp_number}", 320, 350,40,WHITE)
    draw_text(result_text, 280, 400,40, COL)
    draw_text("Press R to Restart", 280, 450,40, WHITE)

    pygame.display.flip()

    # Wait for user to restart
    wait_for_restart()

# Function to restart the game
def wait_for_restart():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                click.play()
                game_loop()  # Restart game

# Main game loop
def game_loop():
    user_input = ""
    running = True
    screen.blit(roll_background_image, (0, 0))
    screen.blit(pause, (750,0 ))
    pygame.display.update()
    
    while running:
        screen.blit(roll_background_image, (0, 0))
        screen.blit(pause, (750,0 ))
        draw_text("Predict a Dice Number (1-6):", 230, 150,43,WHITE)
        draw_text("(Please enter a number between 1 and 6:)", 257, 180,23,WHITE)
        draw_text(user_input, 380, 250,50, GREEN)
        if  user_input.isdigit() and int(user_input) <= 6:
            draw_text("Press Enter to Roll", 280, 350,43, WHITE)
            pygame.display.flip()
        elif user_input.isdigit() and int(user_input) >= 6 :
            draw_text("Invalid!", 340, 350,43, WHITE)
            pygame.display.flip()
        pygame.display.flip()
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                main_page()
            if event.type == pygame.MOUSEBUTTONDOWN  :
                pos = pygame.mouse.get_pos()
                pause_area= button(750,0,pause)
                if pause_area.collidepoint(pos) :
                    click.play()
                    resumemenu3()
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RETURN:  # Roll dice on Enter key
        
                    if user_input.isdigit() and 1 <= int(user_input) <= 6:
                        click.play()
                        roll_dice(int(user_input))
                        return  # Stop loop after rolling
                    else:
                        user_input = "Invalid!"
                        pygame.display.flip()
                        time.sleep(1)
                        user_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]  # Remove last character

                elif event.unicode.isdigit() and len(user_input) < 1:
                    user_input += event.unicode  # Append digit


# To get the area of the button  

def button(x,y,image):
    rect = image.get_rect(topleft=(x, y))
    screen.blit(image, rect)
    return rect 

########################################################

############################################
def resumemenu1():
    global is_muted
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
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
                    a=messagebox.askyesno(title="HOME PAGE",message="Press 'YES' to return to Home")
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
                sys.exit()
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
                    a=messagebox.askyesno(title="HOME PAGE",message="Press 'YES' to return to Home")
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
    while True:
        screen.blit(roll_background_image, (0, 0))
        screen.blit(home_bt, (750,0))
        screen.blit(starting_dice_image, (150,350 ))
        screen.blit(dice_2, (450,350 ))
        draw_text("Select one of the Dice shown below :", 200, 220,35,WHITE)
        pygame.display.update()
        for event in pygame.event.get():
            # To close the screen
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                main_page()
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
                game_button = button(150,350,starting_dice_image)
                roll_button = button(450,350,dice_2)
                if roll_button.collidepoint(pos):
                    click.play()
                    roll2()
                if game_button.collidepoint(pos):
                    click.play()
                    roll()
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
        dice_rolling=[pygame.image.load("Images/roll1.png"),
        pygame.image.load("Images/roll2.png"),
        pygame.image.load("Images/roll3.png"),
        pygame.image.load("Images/roll4.png"),
        pygame.image.load("Images/roll5.png"),
        pygame.image.load("Images/roll6.png"),
        pygame.image.load("Images/roll7.png"),
        pygame.image.load("Images/roll8.png")]
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            #To mute the audio
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                roll_menu()
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
                    for i in range(8):
                        if i <=8:
                            screen.blit(roll_background_image, (0, 0))
                        screen.blit(dice_rolling[i], (170,220 ))
                        screen.blit(dice_rolling[i], (470,220 ))
                        pygame.time.wait(250)
                        pygame.display.update()
                    screen.blit(roll_background_image, (0, 0))
                    screen.blit(roll_button_img, (350, 450))
                    screen.blit(pause, (750, 0))
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

    # Display initial screen
    screen.blit(roll_background_image, (0, 0))
    screen.blit(starting_dice_image, (280, 200))
    screen.blit(roll_button_img, (350, 450))
    screen.blit(pause, (750, 0))
    pygame.display.update()

    # Preload dice rolling images
    dice_rolling = [
        pygame.image.load("Images/roll1.png"),
        pygame.image.load("Images/roll2.png"),
        pygame.image.load("Images/roll3.png"),
        pygame.image.load("Images/roll4.png"),
        pygame.image.load("Images/roll5.png"),
        pygame.image.load("Images/roll6.png"),
        pygame.image.load("Images/roll7.png"),
        pygame.image.load("Images/roll8.png")
    ]

    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                roll_menu()

            # Handle mute/unmute button
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pause_area = button(750, 0, pause)
                if pause_area.collidepoint(pos):
                    click.play()
                    resumemenu1()

                # Check if roll button is clicked
                roll_button = button(350, 450, roll_button_img)
                if roll_button.collidepoint(pos) and not rolling:
                    click.play()
                    rolling = True  # Start dice rolling

        # Perform dice rolling animation
        if rolling:
            pygame.time.delay(300)
            if not is_muted:
                rolling_aud.play()

            # Loop through rolling images
            for i in range(8):  # Fix Index Error
                if i <=8:
                    screen.blit(roll_background_image, (0, 0))
                screen.blit(dice_rolling[i], (300, 220))
                pygame.time.wait(250)
                pygame.display.update()
            # Choose final dice image
            screen.blit(roll_background_image, (0, 0))
            screen.blit(roll_button_img, (350, 450))
            screen.blit(pause, (750, 0))
            pygame.display.update()
            rand_img = random.randint(1, 6)  # Ensure integer
            final_dice_img = pygame.image.load(f"Images/{rand_img}.png")  # Ensure correct path
            screen.blit(final_dice_img, (280, 200))

            if not is_muted:
                rolling_stp_aud.play()

            pygame.event.clear()
            rolling = False  # Stop rolling

        pygame.display.update()
###################################################
def main_page():
    while True:
        screen.blit(main_background_image,(0,0))
        screen.blit(main_image,(310,60))
        screen.blit(roll_bt_img, (160,450 ))
        screen.blit(predict_img, (420,450 ))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # to quit the program
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN : # to check a mouse button is pressed
                pos = pygame.mouse.get_pos() # gets the mouse position
                roll_button = button(160,450,roll_bt_img)
                if roll_button.collidepoint(pos):
                    click.play()
                    roll_menu()
                prd_button = button(420,450,predict_img)
                if prd_button.collidepoint(pos):
                    click.play()
                    game_loop()
                    
#####################################################
main_page()
pygame.display.update()

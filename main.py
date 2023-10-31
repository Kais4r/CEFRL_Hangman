import pygame
import os

# @@@@@@@@@@ user_package import
from Scripts.ui_buttons import Button
from Scripts.Scenes import scene_levelSelection

# @@@@@@@@@@ pygame inition
pygame.init()
pygame.font.init()

# @@@@@@@@@@ One time render
pygame.display.set_caption("CEFRL_Hangman")

# @@@@@@@@@@ Game variables
game_dir = os.path.dirname(__file__)  # get current file location

# @@@@@@@@@@ Display variables
SCREEN_W = 1280
SCREEN_H = 720
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# @@@@@@@@@@ function declaration

# @@@@@@@@@@ define fonts
font = pygame.font.SysFont("arialblack", 60)
# @@@@@@@@@@ define colours
TEXT_COL = (0, 0, 0, 128)

# @@@@@@@@@@ load images
# buttons images
image_dir = game_dir + "\Assets\Images\Buttons"
startBtn_img = pygame.image.load(
    image_dir + "\Button_resume.png").convert_alpha()
quitBtn_img = pygame.image.load(
    image_dir + "\Button_quit.png").convert_alpha()
optionsBtn_img = pygame.image.load(
    image_dir + "\Button_options.png").convert_alpha()
videoBtn_img = pygame.image.load(
    image_dir + "\Button_video.png").convert_alpha()
audioBtn_img = pygame.image.load(
    image_dir + "\Button_audio.png").convert_alpha()
keysBtn_img = pygame.image.load(
    image_dir + "\Button_keys.png").convert_alpha()
backBtn_img = pygame.image.load(
    image_dir + "\Button_back.png").convert_alpha()

resume_button = Button(100, 200, startBtn_img, 1)
options_button = Button(100, 310, optionsBtn_img, 1)
quit_button = Button(100, 420, quitBtn_img, 1)

video_button = Button(100, 200, videoBtn_img, 1)
audio_button = Button(100, 310, audioBtn_img, 1)
keys_button = Button(100, 420, keysBtn_img, 1)
back_button = Button(100, 530, backBtn_img, 1)

# main menu images
mainmenu_hangman_img = pygame.image.load(
    game_dir + "\Assets\Images\Background_img\mainmenu_hangman.png").convert_alpha()


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



# @@@@@@@@@@ game loop
current_scene = "mainmenu"

def changeToOptionsScreen():
    video_button.clicked = True
    audio_button.clicked = True
    back_button.clicked = True

run = True
while run:
    if current_scene == "mainmenu":
        # background
        screen.fill((220, 220, 220))
        screen.blit(mainmenu_hangman_img, [420, 180])
        draw_text("Welcome to CEFRL_Hangman", font, TEXT_COL, 150, 50)

        # draw button
        if resume_button.draw(screen) == True:
            scene_levelSelection.main(True)

        if options_button.draw(screen) == True:
            current_scene = "options"
            changeToOptionsScreen()

        if quit_button.draw(screen) == True:
            run = False

    elif current_scene == "options":
        if video_button.draw(screen) == True:
            print('Video')
        if audio_button.draw(screen) == True:
            print('Audio')
        if keys_button.draw(screen) == True:
            print('Keys')
        if back_button.draw(screen) == True:
            current_scene = "mainmenu"
        # event handler
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            run = False
        pygame.display.update()
        
pygame.quit()
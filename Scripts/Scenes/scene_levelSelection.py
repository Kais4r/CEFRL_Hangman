import pygame
import os
from Scripts.Scenes import scene_game

# @@@@@@@@@@ user_package import
from Scripts.ui_buttons import Button

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

# @@@@@@@@@@ define fonts
font = pygame.font.SysFont("arialblack", 60)
# @@@@@@@@@@ define colours
TEXT_COL = (0, 0, 0, 128)

image_dir = game_dir[:-14] + "\Assets\Images\Buttons"

levelA1Btn_img = pygame.image.load(
    image_dir + "\Button_level_a1.png").convert_alpha()
levelA2Btn_img = pygame.image.load(
    image_dir + "\Button_level_a2.png").convert_alpha()
levelB1Btn_img = pygame.image.load(
    image_dir + "\Button_level_b1.png").convert_alpha()
levelB2Btn_img = pygame.image.load(
    image_dir + "\Button_level_b2.png").convert_alpha()
levelC1Btn_img = pygame.image.load(
    image_dir + "\Button_level_c1.png").convert_alpha()
levelC2Btn_img = pygame.image.load(
    image_dir + "\Button_level_c2.png").convert_alpha()
backBtn_img = pygame.image.load(
    image_dir + "\Button_back.png").convert_alpha()

levelA1_button = Button(775, 140, levelA1Btn_img, 1)
levelA2_button = Button(1000, 140, levelA2Btn_img, 1)
levelB1_button = Button(775, 260, levelB1Btn_img, 1)
levelB2_button = Button(1000, 260, levelB2Btn_img, 1)
levelC1_button = Button(775, 380, levelC1Btn_img, 1)
levelC2_button = Button(1000, 380, levelC2Btn_img, 1)

back_button = Button(775, 550, backBtn_img, 1)

# main menu images
mainmenu_hangman_img = pygame.image.load(
    game_dir[:-14] + "\Assets\Images\Background_img\mainmenu_hangman.png").convert_alpha()

pygame.time.delay(2000)
def main(run):
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    while run:
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            pygame.display.update()

        # background
        screen.fill((220, 220, 220))
        screen.blit(mainmenu_hangman_img, [10, 180])
        draw_text("CERF level select", font, TEXT_COL, 100, 50)

        if levelA1_button.draw(screen) == True:
            scene_game.main(True)
        if levelA2_button.draw(screen) == True:
            scene_game.main(True)
        if levelB1_button.draw(screen) == True:
            scene_game.main(True)
        if levelB2_button.draw(screen) == True:
            scene_game.main(True)
        if levelC1_button.draw(screen) == True:
            scene_game.main(True)
        if levelC2_button.draw(screen) == True:
            scene_game.main(True)
        if back_button.draw(screen) == True:
            run = False

        
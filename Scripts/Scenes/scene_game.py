import pygame
import os
import math
import random

# @@@@@@@@@@@ user import
from Scripts.english_word_list import EnglishWord_List
from Scripts.english_word import EnglishWord
# from Scripts.english_word_list import EnglishWord_List

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RADIUS = 30
GAP = 30
A = 65
FPS = 60

# Fonts
pygame.init()
pygame.font.init()
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 50)
TITLE_FONT = pygame.font.SysFont('comicsans', 20)
DISCRIPTION_FONT = pygame.font.SysFont('comicsans', 40)

# Initialize pygame window
mainWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("CEFRL_Hangman")

# Load images
game_dir = os.path.dirname(__file__)
image_dir = game_dir[:-14] + "\Assets\Images\Character_img"
imageList = [pygame.image.load(os.path.join(
    image_dir, f"hangman{i}.png")).convert_alpha() for i in range(7)]

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Functions

def main(run):
    # Game variables
    def generateButtonLetterList():
        letterList = []
        start_x = round((SCREEN_WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
        start_y = 500

        for i in range(26):
            x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
            y = start_y + ((i // 13) * (GAP + RADIUS * 2))
            letterList.append([x, y, chr(A + i), True])
        return letterList

    def draw():
        mainWindow.fill(WHITE)

        # # Draw title
        # title_text = TITLE_FONT.render("CEFRL Hangman", 1, BLACK)
        # mainWindow.blit(title_text, (SCREEN_WIDTH/2 -
        #                 title_text.get_width()/2, 20))

        # Draw word
        display_word = " ".join(
            [letter if letter in guessed else "_" for letter in word])
        word_text = WORD_FONT.render(display_word, 1, BLACK)
        mainWindow.blit(word_text, (350, 350))

        # Draw letters button for player to choose
        for letter in letterList:
            x, y, letter_str, visible = letter
            if visible:
                pygame.draw.circle(mainWindow, BLACK, (x, y), RADIUS, 3)
                letter_text = LETTER_FONT.render(letter_str, 1, BLACK)
                mainWindow.blit(
                    letter_text, (x - letter_text.get_width()/2, y - letter_text.get_height()/2))

        # Draw hangman according to status
    def draw_hangman(hangman_status):
        mainWindow.blit(imageList[hangman_status], [100, 180])
        pygame.display.update()

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        mainWindow.blit(img, (x, y))

    def display_message(message):
        pygame.time.delay(1000)
        mainWindow.fill(WHITE)
        message_text = WORD_FONT.render(message, 1, BLACK)
        mainWindow.blit(message_text, (SCREEN_WIDTH/2 - message_text.get_width() /
                        2, SCREEN_HEIGHT/2 - message_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)

    # game loop
    clock = pygame.time.Clock()
    # run = True
    while run:
        # prepare for variable for everytime game reset
        # pygame.time.delay(1000)
        playing = True
        mainWindow.fill(WHITE)

        # wordList = english_word_list.GenerateList("A1");

        wordList = ["IDE", "REPLIT", "PYTHON", "PYGAME"]

        wordListTest = EnglishWord_List()
        wordListTest.GenerateList("WORDLIST")
        print(wordListTest.list[0])

        word = random.choice(wordList)

        guessed = []
        letterList = generateButtonLetterList()
        hangman_status = 0

        el = EnglishWord("1","apple", "Trái táo", "dis: Discription section", "synonym test", "level test")


        while playing:
            clock.tick(FPS)
            draw()
            draw_text(el.discription, DISCRIPTION_FONT, BLACK, 350, 50)

            draw_hangman(hangman_status)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    playing = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    for letter in letterList:
                        x, y, letter_str, visible = letter
                        dis = math.sqrt((x - mouseX) ** 2 + (y - mouseY) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(letter_str)
                            if letter_str not in word:
                                hangman_status += 1

            if all(letter in guessed for letter in word):
                display_message("You WON!")
                pygame.time.delay(1250)
                playing = False
            if hangman_status == 6:
                display_message("You NOOB!")
                pygame.time.delay(1250)
                playing = False

# main()
# pygame.quit()

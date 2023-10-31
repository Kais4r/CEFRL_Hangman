import pygame
import os
import math
import random

# @@@@@@@@@@@ user import
from Scripts.english_word_list import EnglishWord_List
from Scripts.ui_buttons import Button
from Scripts.player import Player

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RADIUS = 30
GAP = 35
A = 65
FPS = 60

# Fonts
pygame.init()
pygame.font.init()
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 50)
DISCRIPTION_FONT = pygame.font.SysFont('comicsans', 30)
#UI_FONT = pygame.font.SysFont('comicsans', 20)
HINT_FONT = pygame.font.SysFont('comicsans', 20)

# Initialize pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("CEFRL_Hangman")

# Load images
game_dir = os.path.dirname(__file__)
image_dir = game_dir[:-14] + "\Assets\Images\Character_img"
imageList = [pygame.image.load(os.path.join(
    image_dir, f"hangman{i}.png")).convert_alpha() for i in range(7)]

# Load button
btn_image_dir = game_dir[:-14] + "\Assets\Images\Buttons"
hintBtn_img = pygame.image.load(
    btn_image_dir + "\Button_Hint2.png").convert_alpha()

hint_button = Button(995, 420, hintBtn_img, 1)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Functions

def main(run):
    # Game variables
    def generateButtonLetterList():
        letterList = []
        #start_x = round((SCREEN_WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
        start_x = 10
        start_y = 580

        for i in range(26):
            x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
            y = start_y + ((i // 13) * (GAP + RADIUS * 2))
            letterList.append([x, y, chr(A + i), True])
        return letterList

    def draw():
        screen.fill(WHITE)

        # Draw word
        display_word = " ".join(
            [letter if letter in guessed else "_" for letter in word])
        word_text = WORD_FONT.render(display_word, 1, BLACK)
        screen.blit(word_text, (280, 430))

        # Draw letters button for player to choose
        for letter in letterList:
            x, y, letter_str, visible = letter
            if visible:
                pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 3)
                letter_text = LETTER_FONT.render(letter_str, 1, BLACK)
                screen.blit(
                    letter_text, (x - letter_text.get_width()/2, y - letter_text.get_height()/2))

        # Draw hangman according to status
    def draw_hangman(hangman_status):
        screen.blit(imageList[hangman_status], [50, 280])
        pygame.display.update()

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def display_message(message):
        pygame.time.delay(1000)
        screen.fill(WHITE)
        message_text = WORD_FONT.render(message, 1, BLACK)
        screen.blit(message_text, (SCREEN_WIDTH/2 - message_text.get_width() /
                        2, SCREEN_HEIGHT/2 - message_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)

    # game loop
    clock = pygame.time.Clock()

    #-----Prepare the word list for game
    showedWordList = EnglishWord_List()
    wordListTest = EnglishWord_List()
    # wordList = english_word_list.GenerateList("A1");
    wordListTest.GenerateList("WORDLIST")
    score = 0
    lives = 6
    hints = 2

    hint_button.clicked = True
    # run = True
    currentPlayer = Player("","","","","","","","","","")
    while run:
        # Access player data
        currentPlayer.AccessPlayerData(1)
        #print(currentPlayer.highestScore)

        # prepare for variable for everytime game reset
        # pygame.time.delay(1000)
        playing = True  
        screen.fill(WHITE)

        # When ever player finish guess for one time, change word
        
        # generate a word:
        #example EnglishWord("1","apple", "Trái táo", "dis: Description section", "synonym test", "level test")
        wordTest = random.choice(wordListTest.list)
        #print("word: " + wordTest.name)

        wordExisted = True
        while(wordExisted == True):
            result = "nonExist"
            #check if word already showed    
            for showedWord in showedWordList.list:
                if showedWord.id != wordTest.id:
                    pass
                else:
                    result = "exist"
            
            if result == "exist":
                wordTest = random.choice(wordListTest.list)
            else:
                showedWordList.list.append(wordTest)
                wordExisted = False
        #print("showedWordList lenght: " + str(len(showedWordList.li st)))        
        word = wordTest.name.upper()
        guessed = []
        letterList = generateButtonLetterList()
        hangman_status = 0

        #line1 = line2 = line3 = "                                                                                  test"
        line1 = line2 = line3 = ""
        #print(len(wordTest.description))
        if len(wordTest.description) < 65:
            #line1 = wordTest.description]
            line1 = wordTest.description
        elif 65 < len(wordTest.description) and len(wordTest.description) < 130:
            line1 = wordTest.description[:65]
            line2 = wordTest.description[65:]
        else:
            line1 = wordTest.description[:65]
            line2 = wordTest.description[65:130]
            line3 = wordTest.description[130:]

        # Every play mean guessing one word
        showHint = False
        showHintClicked = 0

        while playing:
            if (lives == 0):
                playing = False
                run = False

            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    playing = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    for letter in letterList:
                        x, y, letter_str, visible = letter
                        if visible:
                            dis = math.sqrt((x - mouseX) ** 2 + (y - mouseY) ** 2)
                            if dis < RADIUS:
                                letter[3] = False
                                guessed.append(letter_str)
                                if letter_str not in word:
                                    hangman_status += 1
                                    lives -= 1
            
            draw()

            # Draw UI element here:
            if hint_button.draw(screen) == True:
                if showHintClicked == 0:
                    if(hints > 0):
                        hints -= 1
                        showHintClicked = 1
                    
                if(showHint == False and showHintClicked == 1):
                    showHint = True
                else:
                    showHint = False    

            draw_text("Description:", WORD_FONT, BLACK, SCREEN_WIDTH/2 - 150, 0)
            draw_text(line1, DISCRIPTION_FONT, BLACK, 30, 70)
            draw_text(line2, DISCRIPTION_FONT, BLACK, 30, 130)
            draw_text(line3, DISCRIPTION_FONT, BLACK, 30, 190)

            draw_text("HighScore: " + str(currentPlayer.highestScore), DISCRIPTION_FONT, BLACK, 1000, 250)
            draw_text("Score: " + str(score), DISCRIPTION_FONT, BLACK, 1000, 290)
            draw_text("Lives: " + str(lives), DISCRIPTION_FONT, BLACK, 1000, 330)
            draw_text("Hint left: " + str(hints), DISCRIPTION_FONT, BLACK, 1000, 370)

            if showHint == True:
                draw_text("Synonym: " + wordTest.synonym, HINT_FONT, BLACK, 280, 250)

            draw_hangman(hangman_status)

            if(score > currentPlayer.highestScore):
                currentPlayer.UpdateHighestScore(score)
            
            if all(letter in guessed for letter in word):
                #display_message("You WON!")
                score += 10
                playing = False
                pygame.time.delay(1000)
            if hangman_status == 6:
                #display_message("You NOOB!")
                playing = False
                pygame.time.delay(1000)

# pygame.quit()

import sys
import pygame
import os
import random
import pygame.font

pygame.init()

xc = 120
yc = 150
griglia = pygame.display.set_mode([530, 590])

# define all card positions:
card1 = pygame.Rect(10, 10, xc, yc)
card2 = pygame.Rect(20+xc, 10, xc, yc)
card3 = pygame.Rect(30+2*xc, 10, xc, yc)
card4 = pygame.Rect(40+3*xc, 10, xc, yc)
card5 = pygame.Rect(10, 20+yc, xc, yc)
card6 = pygame.Rect(20+xc, 20+yc, xc, yc)
card7 = pygame.Rect(30+2*xc, 20+yc, xc, yc)
card8 = pygame.Rect(40+3*xc, 20+yc, xc, yc)
card9 = pygame.Rect(10, 30+2*yc, xc, yc)
card10 = pygame.Rect(20+xc, 30+2*yc, xc, yc)
card11 = pygame.Rect(30+2*xc, 30+2*yc, xc, yc)
card12 = pygame.Rect(40+3*xc, 30+2*yc, xc, yc)

cards = [card1, card2, card3, card4, card5, card6, card7, card8,
         card9, card10, card11, card12]

def game():
    # create a list with all the images that we will possibly use
    griglia = pygame.display.set_mode([530, 590])
    pics0 = []
    pics = []
    for p in os.listdir(r'C:\Users\Matteo\PycharmProjects\MemoryGame'):
        pics0.append(p)
    pics = [picture for picture in pics0 if picture.startswith('Screenshot')]

    # pick 6 random pictures from the list and scale them to the Rect dimensions
    temporary_pic_list = []
    for n in range(1, 7):
        random_pic = pics[random.randint(0, len(pics) - 1)]
        pics.remove(random_pic)
        temporary_pic_list.append(random_pic)
    print(f"\nTemporary_pic_list is: {temporary_pic_list}")

    # create a copy of random chosen images
    temporary_final_double = []
    for doppio in temporary_pic_list:
        temporary_final_double.extend([doppio, doppio])

    # make the allocation random:
    random.shuffle(temporary_final_double)
    print(f"\nTemporary double shuffled list is: {temporary_final_double}")

    # replace every card place with the random chosen pics shuffled
    hidden_item_scaled_list = []
    k = 0
    for shuffle_item in temporary_final_double:
        # convert and scale shuffled pictures
        hidden_item = pygame.image.load(shuffle_item).convert_alpha()
        hidden_item_scaled = pygame.transform.scale(hidden_item, (120, 150))
        # define all the rectangles
        pygame.draw.rect(griglia, (255, 255, 255), cards[k])
        # and put all shuffled scaled pictures on them
        replacement = griglia.blit(hidden_item_scaled, cards[k].topleft)
        k += 1
        # if I append something here I cannot call it as a Rect, because it is Surface element!
        hidden_item_scaled_list.append(hidden_item_scaled)

    # eventually let's create a DICTIONARY to match each card topleft coordinates with a NAME:
    cards_topleft = []
    for item in cards:
        cards_topleft.append(item.topleft)
    reference = dict(zip(cards_topleft, temporary_final_double))

    larghezza = 530
    lunghezza = 590
    griglia = pygame.display.set_mode([larghezza, lunghezza])
    cover = pygame.image.load(r"C:\Users\Matteo\PycharmProjects\MemoryGame\piramidiMessico.jpg").convert_alpha()
    cover_scaled = pygame.transform.scale(cover, (120, 150))

    def draw_rect():
        for i in cards:
            pygame.draw.rect(griglia, (255, 255, 255), i)
            # cover all pictures with default image Piramidi
            griglia.blit(cover_scaled, i.topleft)
    draw_rect()

    # update screen with rectangles:
    pygame.display.flip()

    # variables and conditions for while loop
    score = 0
    pair1 = ''
    pair2 = ''
    pairs_found = []
    firstSelection = None
    secondSelection = None

    def rematch_option():
        # coordinates for the 2 Rect
        xrect = 100
        yrect = 490
        lun_rect = 60
        alt_rect = 40

        # let's create the text to ask for rematch and for 2 options
        rematch_text = str("Would you like to play again?")
        rematch_font = pygame.font.Font(pygame.font.get_default_font(), 22)
        rematch_basso = rematch_font.render(rematch_text, True, (0, 0, 0))

        font_choice = pygame.font.SysFont('Times New Roman', 16, True)
        yes_text = font_choice.render('YAY!', True, (255, 255, 255))
        no_text = font_choice.render('NOPE', True, (255, 255, 255))

        # let's create the 2 Rect for YES and NO replay option.
        # If YES is clicked, replay game (reshuffle), if NO close the game
        yes_rect = pygame.Rect(xrect, yrect, lun_rect, alt_rect)
        no_rect = pygame.Rect(xrect+250, yrect, lun_rect, alt_rect)
        yay = pygame.draw.rect(griglia, (0, 0, 0), yes_rect)
        nope = pygame.draw.rect(griglia, (0, 0, 0), no_rect)

        # let's diplay them when max score is reached
        remach_display = griglia.blit(rematch_basso, (120, 420))
        displayYes = griglia.blit(yes_text, (xrect+lun_rect/6, yrect+alt_rect/4))
        displayNo = griglia.blit(no_text, (xrect+250+lun_rect/6, yrect+alt_rect/4))

        # add mouse click event for YES and NO option
        running = True
        while running:
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if yes_rect.collidepoint(event.pos):
                            starting_screen()
                        elif no_rect.collidepoint(event.pos):
                            sys.exit()
                    pygame.display.update()

    # let's define what will be displayed on screen when finding a pair:
    def text_score():

        score_text = str(f"Good job, you found {score} pair!")
        previous_score_text = str(f"Good job, you found {score-1} pair!")
        win_text = str("Nice, you won!")

        score_font = pygame.font.Font(pygame.font.get_default_font(), 20)

        score_basso = score_font.render(score_text, True, (255, 255, 255))
        previous_score_basso = score_font.render(previous_score_text, True, (0, 0, 0))
        win_basso = score_font.render(win_text, True, (0, 0, 0))

        if score == 1:
            griglia.blit(score_basso, (125, 520))
        elif score > 1 and score < 6:
            griglia.blit(previous_score_basso, (125, 520))
            griglia.blit(score_basso, (125, 520))
        elif score == 6:
            griglia.blit(previous_score_basso, (125, 520))
            griglia.blit(score_basso, (125, 520))
            pygame.time.wait(500)
            griglia.fill((255, 255, 255))
            griglia.blit(win_basso, (190, 260))
            pygame.time.wait(500)

            rematch_option()

    # add mouse-click-event:
    running = True

    while running:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # se clicco la X in alto a destra, chiudo la finestra di gioco:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # se clicco su una carta coperta, mi mostra cosa ce' sotto:
            elif event.type == pygame.MOUSEBUTTONDOWN and score < 6:
                if event.button == 1:
                    for k in range(0, len(cards)):
                        # click on first
                        if pygame.Rect.collidepoint(cards[k], event.pos):
                            if (cards[k][0],cards[k][1]) in pairs_found:
                                pass
                            else:
                                griglia.blit(hidden_item_scaled_list[k], cards[k].topleft)
                                pygame.display.flip()

                                # if we are choosing the first card
                                if firstSelection == None:
                                    firstSelection = [cards[k][0], cards[k][1]]
                                    # print(firstSelection)

                                # if we are chosing the second card
                                else:
                                    secondSelection = [cards[k][0], cards[k][1]]
                                    # print(firstSelection, secondSelection)

                                    # if we select the same card again
                                    if firstSelection == secondSelection:
                                        pass

                                    # if we select another card,
                                    # let's check for the pair by checking
                                    # the NAME of the Screenshot
                                    else:
                                        pair1 = (firstSelection[0], firstSelection[1])
                                        pair2 = (secondSelection[0], secondSelection[1])
                                        if reference[pair1] != reference[pair2]:
                                            # print(f"{reference[pair1]}, {reference[pair2]}, sorry it's not a pair!")
                                            # in this case let's re-cover all cards and start from initial condition of loop
                                            pygame.time.wait(1200)
                                            griglia.blit(cover_scaled, (firstSelection[0], firstSelection[1]))
                                            griglia.blit(cover_scaled, (secondSelection[0], secondSelection[1]))
                                            pygame.display.flip()
                                            firstSelection = None
                                            secondSelection = None

                                        else:
                                            # print(f"{reference[pair1]}, {reference[pair2]}, god job, you found a pair!")
                                            score += 1
                                            text_score()
                                            # let's put pair found coordinates in pairs_found list:
                                            pairs_found.append((firstSelection[0], firstSelection[1]))
                                            pairs_found.append((secondSelection[0], secondSelection[1]))
                                            # after finging a pair, let's "hide" the cards in the pair so they cannot be found even by clicking in that area
                                            # let's create a black card that will serve as a "black background" when a pair is found:
                                            replacement1 = pygame.Rect(firstSelection[0], firstSelection[1], xc, yc)
                                            replacement2 = pygame.Rect(secondSelection[0], secondSelection[1], xc, yc)
                                            if score < 6:
                                                pygame.time.wait(500)
                                                black = pygame.draw.rect(griglia, (0, 0, 0), replacement1)
                                                black = pygame.draw.rect(griglia, (0, 0, 0), replacement2)
                                                pygame.display.flip()
                                            elif score == 6:
                                                griglia.fill((255, 255, 255))
                                                # pygame.time.wait(500)
                                                text_score()
                                                pygame.display.flip()

                                            firstSelection = None
                                            secondSelection = None

#when last pair is found, they should disappeared (they don't do it, BUG)!!

# LET'S START THE GAME WHEN CLICKING ON THE CENTER PICTURE
def starting_screen(xg = 530, yg = 590):

    topx = 125
    topy = 100

    griglia = pygame.display.set_mode([xg, yg])
    cover = pygame.image.load(r"C:\Users\Matteo\PycharmProjects\MemoryGame\piramidiMessico.jpg").convert_alpha()
    centro = pygame.Rect(topx, topy, xg-2*topx, yg-2*topy)
    cover_scaled = pygame.transform.scale(cover, (xg-2*topx, yg-2*topy))
    centro = pygame.draw.rect(griglia, (0, 0, 0), centro)
    griglia.blit(cover_scaled, centro.topleft)

    def text_to_screen():
        text_high = str("Welcome to MEMORY GAME!")
        text_low = str("Click on the image to start the Memory Game")
        font_basso = pygame.font.Font(pygame.font.get_default_font(), 18)
        font_alto = pygame.font.Font(pygame.font.get_default_font(), 24)
        testo_alto = font_alto.render(text_high, True, (255, 255, 255))
        testo_basso = font_basso.render(text_low, True, (255, 255, 255))
        griglia.blit(testo_alto, (85, 50))
        griglia.blit(testo_basso, (70, 520))

    text_to_screen()

    pygame.display.flip()

    pos = pygame.mouse.get_pos()

    running = False
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # if you click on central image, you will start the game
                    if centro.collidepoint(event.pos):
                        game()
        pygame.display.update()

starting_screen()

if __name__ == "__main__":
    pass

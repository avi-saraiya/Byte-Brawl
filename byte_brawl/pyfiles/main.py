import os
import sys
import pygame
from fighter import Fighter

# Function for finding asset files whether running from source or from a PyInstaller bundle
def resource_path(rel_path):
    base = getattr(sys, "_MEIPASS", os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    return os.path.join(base, rel_path)

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# set up screen window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Byte Brawl")

#Create background image
bg_image = pygame.image.load(resource_path("assets/background_image.png")).convert_alpha()

# Loading spritesheets
martial_hero = pygame.image.load(resource_path("assets/MartialHero.png")).convert_alpha()
evil_wizard = pygame.image.load(resource_path("assets/EvilWizard.png")).convert_alpha()

# Defining the number of action animation frames in a list for each character
martial_hero_frames = [4, 4, 7, 8, 3]
evil_wizard_frames = [8, 8, 5, 8, 4]

#Function for drawing background
def print_bg():
    scaled_bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg_image ,(0, 0))

# Function for displaying the health bar
def show_hp(health, x, y):
    health_depletion = health / 100
    pygame.draw.rect(screen, (0, 0, 0), (x - 5, y - 5, 410, 40))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 400, 30))
    pygame.draw.rect(screen, (0, 255, 0), (x, y, (400 * health_depletion), 30))

# Setting a framerate
clock = pygame.time.Clock()
fps = 70

# Getting fonts to be used using a built-in python
countdown_font = pygame.font.SysFont("Arial", 80)
menu_font = pygame.font.SysFont("Arial", 40)

# Defining how long to wait after a fighter dies before showing the menu
menu_delay = 1500 # In milliseconds

# Defining function to display starting countdown
def draw_countdown(text, font, text_col, x, y):
    countdown_img = font.render(text, True, text_col)
    screen.blit(countdown_img, (x, y))

# Defining character frame data to be used elsewhere in the program
martial_hero_frames_height = 208
martial_hero_frames_width = 202.5
martial_hero_scale = 4
martial_hero_offset = [98, 105]
martial_hero_data = [martial_hero_frames_height, martial_hero_frames_width, martial_hero_scale, martial_hero_offset]
evil_wizard_frame_height = 150
evil_wizard_frame_width = 152.5
evil_wizard_scale = 4
evil_wizard_offset = [72, 56]
evil_wizard_data = [evil_wizard_frame_height, evil_wizard_frame_width, evil_wizard_scale, evil_wizard_offset]

# Function for drawing the end of fight menu, returns the button rects for mouse clicks
def draw_menu(winner_text, selection):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))
    winner_img = countdown_font.render(winner_text, True, (255, 0, 0))
    screen.blit(winner_img, winner_img.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)))
    buttons = []
    for i, label in enumerate(["Restart", "Exit"]):
        button = pygame.Rect(0, 0, 300, 70)
        button.center = (SCREEN_WIDTH / 2, 380 + i * 90)
        if i == selection:
            pygame.draw.rect(screen, (255, 0, 0), button)
        else:
            pygame.draw.rect(screen, (60, 60, 60), button)
        pygame.draw.rect(screen, (255, 255, 255), button, 3)
        label_img = menu_font.render(label, True, (255, 255, 255))
        screen.blit(label_img, label_img.get_rect(center=button.center))
        buttons.append(button)
    return buttons

# Function for starting a new fight, creates fresh instances of the fighter class from the fighter.py file
def reset_game():
    player1 = Fighter(1, 200, 410, False, martial_hero_data, martial_hero, martial_hero_frames)
    player2 = Fighter(2, 900, 410, True, evil_wizard_data, evil_wizard, evil_wizard_frames)
    starter_count = 3
    time_last_updated = pygame.time.get_ticks()
    round_over_time = None
    menu_selection = 0
    return player1, player2, starter_count, time_last_updated, round_over_time, menu_selection

player1, player2, starter_count, time_last_updated, round_over_time, menu_selection = reset_game()

run = True
#Create game loop
while run:

    # Setting up the frame rate
    clock.tick(fps)

    #Draw background
    print_bg()

    #Draw the health bar for both players
    show_hp(player1.starting_hp, 40, 20)
    show_hp(player2.starting_hp, 760, 20)

    #Enable player movement
    if starter_count <= -1:
        player1.movement(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player2)
        player2.movement(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player1)
    else:
        if starter_count < 1:
                draw_countdown("Fight!", countdown_font, (255, 0, 0), (SCREEN_WIDTH / 2) - 60, SCREEN_HEIGHT / 3)
        else:
                draw_countdown(str(starter_count), countdown_font, (255, 0, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        if (pygame.time.get_ticks() - time_last_updated) >= 1000: # 1 second == 1000 milliseconds
            starter_count -= 1
            time_last_updated = pygame.time.get_ticks()

    # Updating sprite frames
    player1.update_sprite()
    player2.update_sprite() 

    #Draw players
    player1.draw_character(screen)
    player2.draw_character(screen)

    #Check to see if game over
    winner_text = None
    if player1.alive == False and player2.alive == False:
        winner_text = "Draw !"
    elif player1.alive == False:
        winner_text = "Player 2 wins !"
    elif player2.alive == False:
        winner_text = "Player 1 wins !"

    # Show the winner text, then the menu once the death animation has had time to play
    show_menu = False
    menu_buttons = []
    if winner_text != None:
        if round_over_time == None:
            round_over_time = pygame.time.get_ticks()
        if (pygame.time.get_ticks() - round_over_time) >= menu_delay:
            show_menu = True
            menu_buttons = draw_menu(winner_text, menu_selection)
        else:
            winner_img = countdown_font.render(winner_text, True, (255, 0, 0))
            screen.blit(winner_img, winner_img.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)))

    #Event handler
    menu_choice = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif show_menu:
            # Highlight whichever button the mouse is over
            if event.type == pygame.MOUSEMOTION:
                for i, button in enumerate(menu_buttons):
                    if button.collidepoint(event.pos):
                        menu_selection = i
            # Choose a button by clicking it
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, button in enumerate(menu_buttons):
                    if button.collidepoint(event.pos):
                        menu_choice = i
            # Move between buttons with W/S or the arrow keys, choose with Enter or Space
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP, pygame.K_s, pygame.K_DOWN):
                    menu_selection = 1 - menu_selection
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE):
                    menu_choice = menu_selection

    # Acting on the menu choice: 0 = restart the fight, 1 = exit the game
    if menu_choice == 0:
        player1, player2, starter_count, time_last_updated, round_over_time, menu_selection = reset_game()
    elif menu_choice == 1:
        run = False

    #Update display
    pygame.display.update()

#Exit pygame
pygame.quit()   

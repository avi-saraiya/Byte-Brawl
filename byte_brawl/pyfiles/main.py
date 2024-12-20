import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# set up screen window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("battle_game")

#Create background image
bg_image = pygame.image.load("assets/background_image.png").convert_alpha()

# Loading spritesheets
martial_hero = pygame.image.load("assets/MartialHero.png").convert_alpha()
evil_wizard = pygame.image.load("assets/EvilWizard.png").convert_alpha()

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

#Defining game variables for starting countdown
starter_count = 3
time_last_updated = pygame.time.get_ticks()

# Getting font to be used using a built-in python
countdown_font = pygame.font.SysFont("Arial", 80)

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

# Creating instances of the fighter class from the fighter.py file
player1 = Fighter(1, 200, 410, False, martial_hero_data, martial_hero, martial_hero_frames) 
player2 = Fighter(2, 900, 410, True, evil_wizard_data, evil_wizard, evil_wizard_frames) 

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
    if player1.alive == False:
         draw_countdown("Player 2 wins !", countdown_font, (255, 0, 0), (SCREEN_WIDTH / 2) - 200, SCREEN_HEIGHT / 3)
    if player2.alive == False:
         draw_countdown("Player 1 wins !", countdown_font, (255, 0, 0), (SCREEN_WIDTH / 2) - 200, SCREEN_HEIGHT / 3)

    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Update display
    pygame.display.update()

#Exit pygame
pygame.quit()   

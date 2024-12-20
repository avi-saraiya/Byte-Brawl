import pygame
print("Importing this file...")


class Fighter:
    def __init__(self, player, x, y, flip, character_data, spritesheet, animation_frames): # NOT SURE WHY BUT THIS MUST BE x or y (has something to do with the 'rect' keyword I believe)
        self.player = player
        self.sprite_height = character_data[0]
        self.sprite_width = character_data[1]
        self.sprite_scale = character_data[2] 
        self.sprite_offset = character_data[3]  
        self.get_animation_list = self.get_sprite_frame(spritesheet, animation_frames)
        self.player_action = 0 # 0-attack, 1-idle, 2-death, 3-move, 4-takehit
        self.frame_index = 0
        self.image_displayed = self.get_animation_list[self.player_action][self.frame_index]
        self.update_frame = pygame.time.get_ticks()
        self.flip_player = flip
        self.rect = pygame.Rect(x, y, 80, 180)  
        self.speed_y = 0
        self.is_running = False
        self.has_jumped = False
        self.attacking = False  
        self.attack_cooldown = 0
        self.hit = False
        self.starting_hp = 100 #CHANGE THIS BACK TO 100 
        self.alive = True

    #This functions extracts the images from the spritesheets
    def get_sprite_frame(self, spritesheet, animation_frames):
        animation_master_list = []
        for y_multiplier, animation_frame in enumerate(animation_frames):
            temp_img_list = []
            for x_multiplier in range(animation_frame):
                temp_img = spritesheet.subsurface(x_multiplier * self.sprite_width, y_multiplier * self.sprite_height, self.sprite_width, self.sprite_height)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.sprite_width * self.sprite_scale, self.sprite_height * self.sprite_scale)))
            animation_master_list.append(temp_img_list)
        return animation_master_list

    def attack(self, surface, target):
        if self.attack_cooldown == 0:
            self.attacking = True
            if self.flip_player == False:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip_player), self.rect.y, 2.75 * self.rect.width, self.rect.height)
                #pygame.draw.rect(surface, (0, 0, 255), attacking_rect)
            else:
                attacking_rect = pygame.Rect(self.rect.centerx - (3 * self.rect.width * self.flip_player), self.rect.y, 2.75 * self.rect.width, self.rect.height)
                #pygame.draw.rect(surface, (0, 0, 255), attacking_rect)
            if attacking_rect.colliderect(target.rect):
                target.starting_hp -= 10
                target.hit = True

    def movement(self, screen_width, screen_height, surface, target):
        gravity = 3
        speed_x = 10
        dx = 0
        dy = 0
        self.is_running = False


        # Can only move if player is not attacking
        if not self.attacking and self.alive and target.alive and not self.hit:
            # Player 1 controls
            if self.player == 1:

                # Movement keys
                key = pygame.key.get_pressed()  
                if key[pygame.K_a]:
                    dx = -speed_x
                    self.is_running = True
                    self.flip_player = True

                if key[pygame.K_d]:
                    dx = speed_x
                    self.is_running = True
                    self.flip_player = False

                if key[pygame.K_w] and self.has_jumped == False:
                    self.speed_y = -40
                    self.has_jumped = True

                # Attack keys
                if key[pygame.K_s]:
                    self.attack(surface, target)

            else:
                # Player 2 controls
                key = pygame.key.get_pressed()  
                if key[pygame.K_j]:
                    dx = -speed_x
                    self.is_running = True
                    self.flip_player = True

                if key[pygame.K_l]:
                    dx = speed_x
                    self.is_running = True
                    self.flip_player = False

                if key[pygame.K_i] and self.has_jumped == False:
                    self.speed_y = -40
                    self.has_jumped = True

                # Attack keys
                if key[pygame.K_k]:
                    self.attack(surface, target)
            

        # Jump mechanics
        self.speed_y += gravity
        dy += self.speed_y

        # Keeping the player on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.top + dy < 0:
            dy = -self.rect.top
        if self.rect.bottom + dy > (screen_height - 110):
            self.speed_y = 0
            dy = screen_height - 110 - self.rect.bottom
            self.has_jumped = False

        # Decrementing attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # Making the player sprites always face each other
        '''if target.rect.centerx > self.rect.centerx:
            self.flip_player = False
        else:
            self.flip_player = True'''

        # Update position of player
        self.rect.x += dx
        self.rect.y += dy

    # Function updating sprite display
    def update_sprite(self):
        if self.starting_hp <= 0:
            self.starting_hp = 0
            self.alive = False
            self.update_action(2)
        elif self.hit == True:
            self.update_action(4)
        elif self.attacking == True:
            self.update_action(0)
        elif self.is_running == True:
            self.update_action(3)
        else:
            self.update_action(1)
        time_per_frame = 150 # In milliseconds
        self.image_displayed = self.get_animation_list[self.player_action][self.frame_index]
        if (pygame.time.get_ticks() - self.update_frame) > time_per_frame:
            self.frame_index += 1
            self.update_frame = pygame.time.get_ticks()
        if self.frame_index >= len(self.get_animation_list[self.player_action]):
            # Check if the player is alive before determining animation
            if self.alive == False:
                self.frame_index = len(self.get_animation_list[self.player_action]) - 1 # Stop animation at the last frame
            else:
                self.frame_index = 0 
            if self.player_action == 0: 
                self.attacking = False
                self.attack_cooldown = 50
            if self.player_action == 4:
                self.hit = False
            # If the player is hit, they can't attack at the same time
                self.attacking = False
                self.attack_cooldown = 50


    def update_action(self, new_frame):
        if self.player_action != new_frame:
            self.player_action = new_frame
            self.frame_index = 0
            self.update_frame = pygame.time.get_ticks()

    def draw_character(self, surface):
        flipped_img = pygame.transform.flip(self.image_displayed, self.flip_player, False)
        surface.blit(flipped_img, (self.rect.x - (self.sprite_offset[0] * self.sprite_scale), self.rect.y - (self.sprite_offset[1] * self.sprite_scale)))

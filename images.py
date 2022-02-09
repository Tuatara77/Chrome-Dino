import pygame
import colours

ground = pygame.image.load("./sprites/ground.png")
could = pygame.image.load("./sprites/could.png")
ground.set_colorkey(colours.white)
could.set_colorkey(colours.white)

dino_stationary = pygame.image.load("./sprites/dino/dino-stationary.png")
dino_step_left = pygame.image.load("./sprites/dino/dino-step-left.png")
dino_step_right = pygame.image.load("./sprites/dino/dino-step-right.png")
dino_hit = pygame.image.load("./sprites/dino/dino-hit.png")
dino_crouch_stationary = pygame.image.load("./sprites/dino/dino-crouch-stationary.png")
dino_crouch_left = pygame.image.load("./sprites/dino/dino-crouch-left.png")
dino_crouch_right = pygame.image.load("./sprites/dino/dino-crouch-right.png")
dino_crouch_hit = pygame.image.load("./sprites/dino/dino-crouch-hit.png")

ptera_flap_down = pygame.image.load("./sprites/ptera/ptera-flap-down.png")
ptera_flap_up = pygame.image.load("./sprites/ptera/ptera-flap-up.png")

cactus_1 = pygame.image.load("./sprites/cactus/cactus-1.png")
cactus_1_big = pygame.image.load("./sprites/cactus/cactus-1-big.png")
cactus_2 = pygame.image.load("./sprites/cactus/cactus-2.png")
cactus_2_big = pygame.image.load("./sprites/cactus/cactus-2-big.png")
cactus_3 = pygame.image.load("./sprites/cactus/cactus-3.png")
cactus_4 = pygame.image.load("./sprites/cactus/cactus-4.png")

dino_stationary.set_colorkey(colours.white)
dino_step_left.set_colorkey(colours.white)
dino_step_right.set_colorkey(colours.white)
dino_hit.set_colorkey(colours.white)
dino_crouch_stationary.set_colorkey(colours.white)
dino_crouch_left.set_colorkey(colours.white)
dino_crouch_right.set_colorkey(colours.white)
dino_crouch_hit.set_colorkey(colours.white)

ptera_flap_down.set_colorkey(colours.white)
ptera_flap_up.set_colorkey(colours.white)

cactus_1.set_colorkey(colours.white)
cactus_1_big.set_colorkey(colours.white)
cactus_2.set_colorkey(colours.white)
cactus_2_big.set_colorkey(colours.white)
cactus_3.set_colorkey(colours.white)
cactus_4.set_colorkey(colours.white)

cactuslist = [cactus_1, cactus_1_big, cactus_2, cactus_2_big, cactus_3, cactus_4]
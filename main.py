"""
Controls:
    Jump: W, Up Arrowkey, Space
    Crouch: S, Down Arrowkey
    Pause: Left/Right Shift
    Restart: Tab
    Quit: Escape
"""

import pygame
import random

import spriteclass
import dinoclass
import pteraclass
import otherclasses
import functions
import colours

# Changeables
FPS = 60
SCROLLRATE = 7
GRAVITY = 15
PAUSE = False

# Constants - DO NOT CHANGE (except from screenwidth and screenheight - change at your own risk)
SCREENWIDTH, SCREENHEIGHT = 800, 400
TILESIZE = 40
PLAYERCOORDX, PLAYERCOORDY = 5*TILESIZE, SCREENHEIGHT-3*TILESIZE

# Variables that shouldn't be changed
count = 0
score = 0


def drawscreen():
    pygame.display.set_caption(f"Dino - Score: {score}")
    screen.fill(colours.white)
    otherclasses.cloudg.draw(screen)
    otherclasses.cactusg.draw(screen)
    otherclasses.groundg.draw(screen)
    pteraclass.pterag.draw(screen)
    dinoclass.dinog.draw(screen)
    screen.blit(text.render(f"Score: {score}", True, colours.black), (0,0))
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
pygame.display.set_caption(f"Dino - Score: {score}")

dino = dinoclass.Dino(PLAYERCOORDX, PLAYERCOORDY)

text = pygame.font.Font(pygame.font.get_default_font(), 20)
clock = pygame.time.Clock()
functions.groundspawn()

done = False
while not done: # mainloop
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_TAB:
                for thing in spriteclass.spriteg:
                    thing.restart()
                count = 0
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                if not PAUSE:
                    PAUSE = True
                    SCROLLRATE = 0
                else:
                    PAUSE = False
                    SCROLLRATE = 7

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
        dino.jump(GRAVITY)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if not dino.crouch:
            dino.crouch = True
    else:
        if dino.crouch:
            dino.crouch = False

    dino.fall(GRAVITY)
    dead = dino.collide()
    if dead:
        count, score = 0,0

    count += 1
    if count % 4 == 0 and not PAUSE:
        score += 1
    
    if count % random.randrange(70,140,35) == 0 and not PAUSE:
        choice = random.choice([1,2,3,4])
        if choice == 1:
            functions.spawnptera()
        else:
            functions.spawncactus()
    if count % random.randrange(70,560,70) == 0 and not PAUSE:
        functions.spawncloud()

    for thing in spriteclass.spriteg:
        if thing.rect.right < -TILESIZE:
            if thing in otherclasses.groundg:
                thing.rect.left = SCREENWIDTH+TILESIZE
            else:
                thing.kill()
        if not PAUSE:
            thing.scroll(SCROLLRATE, count)

    drawscreen()
pygame.quit()
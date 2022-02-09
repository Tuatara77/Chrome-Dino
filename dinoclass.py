import pygame
import time
import spriteclass
import pteraclass
import otherclasses
import images

screenwidth, screenheight = 800, 400
tilesize = 40
playercoordx, playercoordy = 5*tilesize, screenheight-3*tilesize

dinog = pygame.sprite.Group()

class Dino(spriteclass.Sprite):
    def __init__(self, x, y):
        super().__init__(x,y,images.dino_stationary)

        self.dy = 0
        self.crouch = False
        self.falling = False
        self.grounded = True

        dinog.add(self)
    
    def restart(self):
        self.image = images.dino_stationary
        self.rect.left = self.startx
        self.rect.bottom = self.starty
        self.dy = 0
        self.falling = False
        self.grounded = True
        self.crouch = False

    def scroll(self, scrollrate, count):
        if count % 8 == 0:
            if not self.crouch and not self.falling:
                if self.image != images.dino_step_left and self.image != images.dino_step_right:
                    self.image = images.dino_step_left
                    self.rect = self.image.get_rect()
                    self.rect.left = playercoordx
                    self.rect.bottom = playercoordy
                    # drawscreen()
                
                elif self.image == images.dino_step_right:
                    self.image = images.dino_step_left
                elif self.image == images.dino_step_left:
                    self.image = images.dino_step_right

            elif not self.crouch and self.falling:
                self.image = images.dino_stationary
            
            elif self.crouch and not self.falling:
                if self.image != images.dino_crouch_left and self.image != images.dino_crouch_right:
                    self.image = images.dino_crouch_left
                    self.rect = self.image.get_rect()
                    self.rect.left = playercoordx
                    self.rect.bottom = playercoordy
                    # drawscreen()

                elif self.image == images.dino_crouch_right:
                    self.image = images.dino_crouch_left
                elif self.image == images.dino_crouch_left:
                    self.image = images.dino_crouch_right
            
            elif self.crouch and self.falling:
                self.image = images.dino_crouch_stationary

    def fall(self, gravity):
        if self.falling:
            self.dy += 1
        if self.dy > gravity:
            self.dy = gravity
        
        self.rect.y += self.dy

    def jump(self, gravity):
        if self.grounded:
            self.image = images.dino_stationary
            self.dy = -gravity
            self.falling = True
            self.grounded = False

    def collide(self):
        groundcollide = pygame.sprite.spritecollide(self, otherclasses.groundg, False)
        for land in groundcollide:           
            self.rect.bottom = land.rect.top
            self.grounded = land
            self.falling = False
            self.dy = 0
        
        cactuscollide = pygame.sprite.spritecollide(self, otherclasses.cactusg, False)
        pteracollide = pygame.sprite.spritecollide(self, pteraclass.pterag, False)
        if cactuscollide or pteracollide:
            if self.crouch:
                self.image = images.dino_crouch_hit
            else:
                self.image = images.dino_hit
            # drawscreen()
            time.sleep(0.75)
            for thing in spriteclass.spriteg:
                if thing not in otherclasses.groundg and thing not in dinog:
                    thing.kill()
                else:
                    thing.restart()
            return True
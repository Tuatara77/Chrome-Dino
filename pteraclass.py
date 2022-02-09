import pygame
import spriteclass
import images

screenwidth, screenheight = 800, 400
tilesize = 40
pteraheights = [screenheight-3*tilesize-3, screenheight-4*tilesize-3, screenheight-5*tilesize-3]

pterag = pygame.sprite.Group()

class Ptera(spriteclass.Sprite):
    def __init__(self,x,y):
        super().__init__(x,y,images.ptera_flap_down)
        pterag.add(self)
    
    def scroll(self, scrollrate, count):
        self.rect.x -= scrollrate
        if count % 12 == 0:
            if self.image == images.ptera_flap_down:
                self.tempx = self.rect.left
                self.tempy = self.rect.bottom
                self.image = images.ptera_flap_up
                self.rect = self.image.get_rect()
                self.rect.left = self.tempx
                self.rect.bottom = self.tempy
            elif self.image == images.ptera_flap_up:
                self.tempx = self.rect.left
                self.tempy = self.rect.bottom
                self.image = images.ptera_flap_down
                self.rect = self.image.get_rect()
                self.rect.left = self.tempx
                self.rect.bottom = self.tempy
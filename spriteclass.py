import pygame

spriteg = pygame.sprite.Group()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.left = x
        self.rect.bottom = y # makes bottom left corner be the point of reference
        self.startx = x
        self.starty = y

        spriteg.add(self)
    
    def scroll(self, scrollrate, count):
        self.rect.x -= scrollrate
    
    def restart(self):
        self.rect.left = self.startx
        self.rect.bottom = self.starty
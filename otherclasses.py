import pygame
import spriteclass
import images

cactusg = pygame.sprite.Group()
groundg = pygame.sprite.Group()
cloudg = pygame.sprite.Group()

class Cactus(spriteclass.Sprite):
    def __init__(self, x, y, image):
        super().__init__(x,y,image)
        cactusg.add(self)

class Ground(spriteclass.Sprite):
    def __init__(self,x,y,image):
        super().__init__(x,y,image)
        groundg.add(self)

class Cloud(spriteclass.Sprite):
    def __init__(self,x,y):
        super().__init__(x,y,images.could)
        cloudg.add(self)

    def scroll(self, scrollrate, count):
        self.rect.x -= 1
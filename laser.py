import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed, constraints):
        super().__init__() 
        self.image = pygame.image.load('Graphics//Charge_1.png')
        self.image = pygame.transform.rotozoom(self.image, 90, 0.4)
        self.rect = self.image.get_rect(midbottom=(pos_x, pos_y))
        self.speed = speed
        self.constraints = constraints
    def destroy(self):
        if self.rect.y < 0 or self.rect.y > self.constraints + 3:
            self.kill()
    def update(self):
        self.rect.y -= self.speed
        self.destroy()

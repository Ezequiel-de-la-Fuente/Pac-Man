import pygame
from pygame import sprite, image, transform, draw,mask
import configuration        
class Wall(sprite.Sprite):
    def __init__(self,image_path : str,pos = (0,0)):
        super().__init__()
        self.image = image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    
    def update(self):
        super().update()
        
        
    
    
    
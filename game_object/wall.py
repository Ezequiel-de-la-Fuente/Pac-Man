import pygame
from pygame import sprite, image, transform, draw,mask
import configuration    
from game_object.wall_model import WallModel    
class Wall(sprite.Sprite):
    def __init__(self,wall_model:WallModel,pos = (0,0)):
        super().__init__()
        self.image = wall_model.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    
    def update(self):
        super().update()
        
        
    
    
    
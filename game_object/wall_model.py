import pygame
from pygame import sprite, image, transform, draw,mask
import configuration
class WallModel(sprite.Sprite):
    def __init__(self):
        super().__init__()  
        self.image = image.load('data/sprite/wall/wall_0.png').convert_alpha()
        self.rect = pygame.Rect(0,0,0,0)
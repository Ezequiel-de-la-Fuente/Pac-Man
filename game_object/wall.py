import pygame
from pygame import sprite, image, transform, draw
import configuration

class Wall():
    def __init__(self,color : tuple, pos = (0,0), tam = (0,0)):
        super().__init__()
        self.rect = pygame.Rect(0,0,0,0)
        self.x = pos[0]
        self.y = pos[1]
        self.width = tam[0]
        self.height = tam[1]
        self.color = color
        
    def draw(self,screen):
        self.rect = draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
    
    
    
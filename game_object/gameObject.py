import pygame
from pygame import sprite, image

class GameObject(sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image = image.load('data/sprite/player/example.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 300
        
        self._speed_x = 0
        self._speed_y = 0
        
        self._is_alive = True
        
        self._animState = {"idle":True, "run_loop":False, "death":False}
        self._images = []
        
    def get_speed(self):
        return (self._speed_x,self._speed_y)
    
    def set_speed(self, speed_x=0,speed_y=0):
        self._speed_x = speed_x
        self._speed_y = speed_y
    def get_is_alive(self):
        return self._isAlive
    
    def get_animState(self):
        return self._animState
    
    def get_images(self):
        return self._images
    
    def update(self):
        self.rect.x += self._speed_x
        self.rect.y += self._speed_y
    
    def __update_anim(self):
        #TODO: Hacer este caso de uso
        pass
    
    def __out_screen(self):
        #TODO: Hacer este caso de uso
        pass
    
    def _set_color(self, color):
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(color)
        self.image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        
    def _cheack_walls(self,walls=[]):
        for wall in walls:
            if self.rect.colliderect(wall):
                dx,dy = self.get_speed()
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.bottom
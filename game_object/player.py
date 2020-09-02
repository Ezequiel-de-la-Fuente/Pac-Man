import pygame
from pygame import sprite, image

from game_object.gameObject import GameObject
class Player(GameObject):
    _NORMAL_SPEED = 4
    def __init__(self,color):
        super().__init__(color)
        self.image = image.load('data/sprite/player/example.png').convert()
        self._set_color(color)
        self._special_atack = {"shoot_laser":False,"stop_time":False,"atack_on":False}
        self._score = 0
        self._speed_boost = 5
    
    def update(self,walls):
        super().update()
        self._cheack_walls(walls=walls)
    
    def check_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.set_speed(0,-Player._NORMAL_SPEED)
            if event.key == pygame.K_s:
                self.set_speed(0,Player._NORMAL_SPEED)
            if event.key == pygame.K_a:
                self.set_speed(-Player._NORMAL_SPEED,0)
            if event.key == pygame.K_d:
                self.set_speed(Player._NORMAL_SPEED,0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and self.get_speed()[1] == -Player._NORMAL_SPEED:
                self.set_speed(0,0)
            if event.key == pygame.K_s and self.get_speed()[1] == Player._NORMAL_SPEED:
                self.set_speed(0,0)
            if event.key == pygame.K_a and self.get_speed()[0] == -Player._NORMAL_SPEED:
                self.set_speed(0,0)
            if event.key == pygame.K_d and self.get_speed()[0] == Player._NORMAL_SPEED:
                self.set_speed(0,0)
            

    def check_coin_type(self, coin):
        #TODO: Hacer este caso de uso
        pass
    
    
    def __shoot_laser(self):
        #TODO: Hacer este caso de uso
        pass
    
    def __pause_time(self):
        #TODO: Hacer este caso de uso
        pass
    
    def __atack_on(self):
        #TODO: Hacer este caso de uso
        pass    
    
    
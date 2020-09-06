import pygame
import math
import random
from pygame import sprite, image, time,transform
from audio_source import AudioSource
from game_object.gameObject import GameObject
from game_object.player import Player

class Ghost(GameObject):
    def __init__(self, color, x=370,y=320):
        super().__init__(color)
        self.image = image.load('data/sprite/ghost/red/red_ghost_0.png').convert_alpha()
        # self._set_color(color)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.__max_speed = 4
        self.set_speed(0,self.__max_speed)
        self.audioSource = AudioSource()
        # self.audioSource.add_audio_clip('data/sound/Point.wav','beat',0.1)
    
    def update(self,player : Player,walls):
        super().update()
        self._cheack_walls(walls,player)
        
    def distance(self, x_player : int, y_player : int):
        return math.sqrt(pow(self.dx(x_player),2) + pow(self.dy(y_player),2))

    def dx(self, x_player):
        return self.rect.x - x_player
    
    def dy(self, y_player):
        return self.rect.y - y_player
    
    def _cheack_walls(self,walls,player : Player):
        result = False
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                result = self.rect.colliderect(wall.rect)
                dx,dy = self.get_speed()
                # print(self.distance(player.rect.x,player.rect.y))
                rand = random.randint(0,2)
                
            
                
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                    if rand == 0:
                        self.up(self.__max_speed)
                    elif rand == 1:
                        self.left(self.__max_speed)
                    elif rand == 2:
                        self.down(self.__max_speed)
                        
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    if rand == 0:
                        self.down(self.__max_speed)
                    elif rand == 1:
                        self.right(self.__max_speed)
                    elif rand == 2:
                        self.up(self.__max_speed)
                        
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                    if rand == 0:
                        self.right(self.__max_speed)
                    elif rand == 1:
                        self.up(self.__max_speed)
                    elif rand == 2:
                        self.left(self.__max_speed)
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    if rand == 0:
                        self.left(self.__max_speed)
                    elif rand == 1:
                        self.down(self.__max_speed)
                    elif rand == 2:
                        self.right(self.__max_speed)
        return result
    
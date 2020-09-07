import pygame
import math
import random

import pathfinding.core.diagonal_movement,pathfinding.core.grid,pathfinding.finder.a_star

from pygame import sprite, image, time,transform
from audio_source import AudioSource

from game_object.gameObject import GameObject
from game_object.player import Player

class Ghost(GameObject):
    def __init__(self, color,level = "", x=370,y=320):
        super().__init__(color)
        self.image = image.load('data/sprite/ghost/red/red_ghost_0.png').convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.__max_speed = 4
        self.set_speed(0,self.__max_speed)
        self.audioSource = AudioSource()
        
        self.current_level = Ghost._matrix_str_to_matrix_int(level)
        self.initial_level_form = self.current_level.copy()
        
        self.find_time = 0
        self.restart_time = -1
        self.current_path = []
        self.aux = ()
        
        self.find_path = False
        self.delay_time = -1
        # self.audioSource.add_audio_clip('data/sound/Point.wav','beat',0.1)
    
    def update(self,player : Player,walls):
        super().update()
        self._cheack_walls(walls,player)
            
            
        if self.distance(player.rect.x, player.rect.y) < 200:
            if not self.find_path and self.restart_time<time.get_ticks():
                # self.stop_move()
                self.iteration = 0
                self.iteration_time = 0
                grid = pathfinding.core.grid.Grid(matrix=self.current_level)
                
                x_ghost,y_ghost = self.get_pos()
                x_player,y_player = player.get_pos()
                
                start = grid.node(x_ghost, y_ghost)
                try:
                    end = grid.node(x_player, y_player)
                except IndexError as Error:
                    end = grid.node(1,1)
                
                
                finder = pathfinding.finder.a_star.AStarFinder(diagonal_movement=pathfinding.core.diagonal_movement.DiagonalMovement.never)
                
                path, runs = finder.find_path(start, end, grid)
                
                # self.current_path = list(path)
                for e in path:
                    self.current_path.append(e)
                self.current_path.pop(0)
                # print(self.current_path)
                self.find_path = True
                self.find_time = time.get_ticks() + 2000
                
        if self.find_path:
            # print("Te busco")
            if len(self.current_path)==0:
                self.find_path = False
                self.restart_time = time.get_ticks() + 10000
                self.current_path.clear()
            elif self.find_time < time.get_ticks():
                self.find_path = False
                self.current_path.clear()
                self.restart_time = time.get_ticks() + 4000
            else:
                dx = self.get_pos()[0] - self.current_path[0][0]
                dy = self.get_pos()[1] - self.current_path[0][1]
                if self.delay_time>time.get_ticks():
                    dx = self.get_pos()[0] - self.aux[0]
                    dy = self.get_pos()[1] - self.aux[1]
                if dx==1:
                    self.left(self.__max_speed)
                    
                elif dx==-1:
                    self.right(self.__max_speed)
                elif dy==1:
                    self.up(self.__max_speed)
                elif dy==-1:
                    self.down(self.__max_speed)
                    
                if self.get_pos()==self.current_path[0] and self.delay_time<time.get_ticks():
                    self.aux = self.current_path.pop(0)
                    speed_x, speed_y = self.get_speed()
                    if speed_y == 4:
                        self.delay_time=time.get_ticks() + 10
                    elif speed_y == -4:
                        self.delay_time=time.get_ticks() + 200
                        
                    if speed_x == 4:
                        self.delay_time=time.get_ticks() + 40
                    elif speed_x == -4:
                        self.delay_time=time.get_ticks() + 200
                    
                    
            
                
        
        
    def distance(self, x_player : int, y_player : int):
        return math.sqrt(pow(self.dx(x_player),2) + pow(self.dy(y_player),2))

    def dx(self, x_player):
        return self.rect.x - x_player
    
    def dy(self, y_player):
        return self.rect.y - y_player
    
    
    def _cheack_walls(self,walls,player : Player, rand = -1):
        result = False
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                result = self.rect.colliderect(wall.rect)
                dx,dy = self.get_speed()
                if rand==-1:
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
    
    @staticmethod
    def _matrix_str_to_matrix_int(matrix):
        index = 0
        new_matrix = []
        for i in matrix:
            new_matrix_2 = []
            for j in matrix[index]:
                if j =='W':
                    new_matrix_2.append(0)
                else:
                    new_matrix_2.append(1)
            new_matrix.append(new_matrix_2)
            index+=1
        return new_matrix
    
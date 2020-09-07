import pygame
from pygame import sprite, image, time,transform
from audio_source import AudioSource
from game_object.gameObject import GameObject
from PIL import Image

class Player(GameObject):
    def __init__(self,color, x = 300,y=300):
        super().__init__(color)
        for i in range(8):
            self._images.append(image.load('data/sprite/player/sprite_{}.png'.format(i)).convert_alpha())
        self.index = 0
        
        
        self.image = self._images[self.index]
        self.images_right = self._images
        self.images_left = [transform.flip(image_,True,False) for image_ in self._images]
        self.images_down = [transform.rotate(image_,-90)for image_ in self.images_right]
        self.images_up = [transform.rotate(image_,90)for image_ in self.images_right]
        self.time_animation = 0
        self.number_of_frames = 8
        self.rect = self.image.get_rect()
        
        self.isFlip = False 
        
        self.rect.x = x
        self.rect.y = y
        self.__max_speed = 4
        
        self.rotate_down = False
        self.rotate_up = False
        
        self._special_atack = {"shoot_laser":False,"stop_time":False,"atack_on":False}
        self._score = 0
        self._speed_boost = 5
        
        self.audioSource = AudioSource()
        self.audioSource.add_audio_clip('data/sound/Point.wav','beat',0.1)
        self.__actual_time = 0
    
    def update(self,walls):
        super().update()
        self._cheack_walls(walls=walls)
        if self.isFlip:
            self._images = self.images_left
        else:
            self._images = self.images_right
        if self.rotate_down:
                self._images = self.images_down
        elif self.rotate_up:
            self._images = self.images_up
        if self._speed_x != 0 or self._speed_y != 0:
            if self.time_animation<time.get_ticks():
                self.time_animation = time.get_ticks() + 100
            else:
                self.index+=1
                if self.index>self.number_of_frames-1:
                    self.index = 0
                self.image = self._images[self.index]
    
    def check_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.up(self.__max_speed)
                self.isFlip = False
                self.rotate_down = False
                self.rotate_up = True
            if event.key == pygame.K_s:
                self.down(self.__max_speed)
                self.rotate_down = True
                self.rotate_up = False
            if event.key == pygame.K_a:
                self.left(self.__max_speed)
                self.isFlip = True
                self.rotate_down = False
                self.rotate_up = False
            if event.key == pygame.K_d:
                self.right(self.__max_speed)
                self.isFlip = False
                self.rotate_down = False
                self.rotate_up = False
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and self.get_speed()[1] == -self.__max_speed:
                self.stop_move()
            if event.key == pygame.K_s and self.get_speed()[1] == self.__max_speed:
                self.stop_move()
            if event.key == pygame.K_a and self.get_speed()[0] == -self.__max_speed:
                self.stop_move()
            if event.key == pygame.K_d and self.get_speed()[0] == self.__max_speed:
                self.stop_move()

    

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
    
    
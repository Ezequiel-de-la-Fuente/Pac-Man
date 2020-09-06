import pygame
from pygame import sprite, image, time,transform
from audio_source import AudioSource
from game_object.gameObject import GameObject
class Player(GameObject):
    def __init__(self,color, x = 300,y=300):
        super().__init__(color)
        self.image = image.load('data/sprite/player/sprite_0.png').convert_alpha()
        self.rect = self.image.get_rect()
        # self.rect.inflate_ip(-5,-5)
        self.rect.x = x
        self.rect.y = y
        self.__max_speed = 4
        
        self._special_atack = {"shoot_laser":False,"stop_time":False,"atack_on":False}
        self._score = 0
        self._speed_boost = 5
        
        self.audioSource = AudioSource()
        self.audioSource.add_audio_clip('data/sound/Point.wav','beat',0.1)
        self.__actual_time = 0
    
    def update(self,walls):
        super().update()
        self._cheack_walls(walls=walls)
        # if not self._speed_x==0 or not self._speed_y==0:
        #     self.audioSource.play_audio_clip_each('beat',300)
        # else:
        #     self.audioSource.stop_audio_clip('beat')
    
    def check_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.up(self.__max_speed)
            if event.key == pygame.K_s:
                self.down(self.__max_speed)
            if event.key == pygame.K_a:
                self.left(self.__max_speed)
            if event.key == pygame.K_d:
                self.right(self.__max_speed)
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
    
    
import pygame
from pygame import sprite, image, time,transform
from audio_source import AudioSource
from game_object.gameObject import GameObject
import color
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
        self.dead_image = []
        for i in range(10):
            self.dead_image.append(image.load('data\\sprite\\player\\dead\\dead_0{}.png'.format(i)).convert_alpha())
        for i in range(10,13):
            self.dead_image.append(image.load('data\\sprite\\player\\dead\\dead_{}.png'.format(i)).convert_alpha())
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
        self.audioSource.add_audio_clip('data\\sound\\power_up.wav','power_up',0.3)
        self.audioSource.add_audio_clip('data\\sound\\death.wav','death',0.3)
        self.__actual_time = 0
        self.__atack_time = -1
        self.__pause_time = 0
        self.anim_on = False
        self.play_death_sound = False
    def update(self,walls, ghosts):
        super().update()
        
        self._cheack_walls(walls=walls)
        self.__check_ghosts(ghosts)
        
                
        if not self._is_alive:
            self.stop_move()
            if not self.play_death_sound:
                self.audioSource.stop_music()
                self.audioSource.play_audio_clip('death')
                self.play_death_sound = True
            self._images = self.dead_image
            if self.time_animation<time.get_ticks():
                self.time_animation = time.get_ticks() + 50
                self.anim_on = True
            elif self.anim_on:
                self.anim_on = False
                self.dead_animation()
        else:
            self.__change_image()
            
        if self._special_atack['atack_on']: 
            if self.__atack_time==-1:
                self.__atack_time = time.get_ticks() + 15000
            elif self.__atack_time<time.get_ticks():
                self.__atack_time = -1
                self._special_atack['atack_on']=False
        if self._special_atack['stop_time']: 
            if self.__atack_time==-1:
                self.__atack_time = time.get_ticks() + 15000
            elif self.__atack_time<time.get_ticks():
                self.__atack_time = -1
                self._special_atack['stop_time']=False
        
    def dead_animation(self):
        self.index+=1
        if self.index<13:
            self.image = self._images[self.index]

    def __change_image(self):
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

    def __check_ghosts(self, ghosts):
        for ghost in ghosts:
            if self.rect.colliderect(ghost.rect):
                if self._special_atack['atack_on']:
                    ghost._is_alive = False
                    # ghost.rect.x = 370
                    # ghost.rect.y = 320
                elif ghost.atack:
                    self._is_alive = False
            elif self._special_atack['stop_time'] and ghost.get_max_speed() == 4:
                ghost.set_max_speed(1)
                ghost.stop_move()
                ghost.up(1)
            elif not self._special_atack['stop_time'] and ghost.get_max_speed() == 1:
                ghost.set_max_speed(4)
                ghost.up(4)
    
    def check_input(self, event):
        if self.get_is_alive():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.up(self.__max_speed)
                    self.__flip_and_rotate(False,False,True) 
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.down(self.__max_speed)
                    self.__flip_and_rotate(False,True,False)
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.left(self.__max_speed)
                    self.__flip_and_rotate(True,False,False)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.right(self.__max_speed)
                    self.__flip_and_rotate(False,False,False)
                    
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.get_speed()[1] == -self.__max_speed:
                    self.stop_move()
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.get_speed()[1] == self.__max_speed:
                    self.stop_move()
                if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.get_speed()[0] == -self.__max_speed:
                    self.stop_move()
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.get_speed()[0] == self.__max_speed:
                    self.stop_move()

    def __flip_and_rotate(self, isFlip : bool, rotete_down : bool, rotate_up : bool):
        self.isFlip = isFlip
        self.rotate_down = rotete_down
        self.rotate_up = rotate_up

    
    def check_coin_type(self, coin):
        sound = False
        if coin.coin_model.color == color.YELLOW:
            self._special_atack['atack_on'] = True
            sound = True
        if coin.coin_model.color == color.BLUE:
            self._special_atack['stop_time'] = True
            sound = True
        if sound:
            self.audioSource.play_audio_clip('power_up')
            #agregar un tiempo de ataque
    
    
    def __shoot_laser(self):
        #TODO: Hacer este caso de uso
        pass
    
    # def __pause_time(self):
    #     #TODO: Hacer este caso de uso
    #     pass
    
    def __atack_on(self):
        #TODO: Hacer este caso de uso
        pass 
    def get_time_atack(self):
        return self.__atack_time
    
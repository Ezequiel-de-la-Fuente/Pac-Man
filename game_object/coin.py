import pygame
from pygame import sprite, image
from game_object.coin_model import CoinModel
class Coin():
    _id=0
    def __init__(self, coin_model : CoinModel, pos : tuple, score):
        super().__init__()
        self.id = Coin._id
        self.score = score
        self.coin_model = coin_model
        self.pos = pos
        self.rect = pygame.Rect(0,0,0,0)
        self.radio = 1
        Coin._id+=1
        
    def draw(self, screen):
        self.rect = screen.blit(self.coin_model.image,self.pos)
        
        
    def get_rect(self):
        return self.rect
    
    def play_sound(self):
        self.coin_model.audioSource.play_audio_clip('coin')
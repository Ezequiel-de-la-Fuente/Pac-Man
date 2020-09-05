import pygame
from pygame import sprite, image, transform
from audio_source import AudioSource
class CoinModel(sprite.Sprite):
    def __init__(self,color : tuple,scale : tuple):
        super().__init__()
        self.image = image.load('data/sprite/coin_model.png').convert()
        self._set_color(color)
        self.color = color
        self.audioSource = AudioSource()
        self.audioSource.add_audio_clip('data/sound/sfx_coin_double1.wav','coin',0.5)
    
    def _set_color(self, color : tuple):
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(color)
        self.image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
    
    
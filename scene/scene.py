import pygame
from pygame import font,time, display
from audio_source import AudioSource
import configuration, color
class Scene():
    def __init__(self):
        self.screen = display.set_mode(size=(configuration.SCREEN_WIDTH,configuration.SCREEN_HEIGHT))
        self._state = {'continue':False, 'exit':False}
        self._clock = time.Clock()
        self._fps = 30
        self.audio_source = AudioSource()
        
    def process(self):
        pass
    def display_frame(self):
        pass
    def _draw_text(self, font, text : str, x : int, y : int):
        text_Obj = font.render(text,1,color.WHITE,self.screen)
        text_rect = text_Obj.get_rect()
        text_rect.topleft = (x,y)
        self.screen.blit(text_Obj, text_rect)
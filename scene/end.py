import sys
import pygame
from pygame import display, font, sprite, time, event
import color
import configuration
# from audio_source import AudioSource
# from game_object.player import Player
# from game_object.ghost import Ghost
# from game_object.dead_ghost_model import DeadGhostModel
# from coin_model_factory import CoinModelFactory,Coin
# from game_object.wall import Wall
# from game_object.wall_model import WallModel
from pygame import font
from ui.input_box import InputBox
from scene.scene import Scene

class End(Scene):
    def __init__(self, score : int, name_score_list : []):
        super().__init__()
        self.input_box = InputBox(600,100,30,60)
        self.tittle_text = "HIGHT SCORES"
        self.tittle_font = font.Font('data\\dpcomic.ttf',40)
        self.name_font = font.Font('data\\dpcomic.ttf',55)
        self.score_font = font.Font('data\\dpcomic.ttf',20)
        self.name_score_list = name_score_list
        self.score = score
        
    
    def process(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.input_box.handle_event(event)

        self.input_box.update()

        
    def display_frame(self):
        self.screen.fill(color.BLACK)
        
        self.input_box.draw(self.screen)
        
        
        end = self.input_box.end
        
        self._draw_text(self.tittle_font,self.tittle_text,30,10)
        self._draw_text(self.name_font,"NAME: ",450,110)
        self._draw_text(self.name_font,"SCORE: {}".format(self.score),450,170)
        len_ = len(self.name_score_list)
        if len_>10:
            len_=10
                   
        for i in range(len_):
            name = self.name_score_list[i][0]
            score = self.name_score_list[i][1]
            self._draw_text(self.score_font,"{}) {}: {}".format(i+1,name,score),20,80 + 25*i)
        
        pygame.display.flip()
        self._clock.tick(self._fps)

def main(score,lst):
    pygame.init()
    my_end = End(score,lst)
    end = False
    while not end:
        my_end.process()
        my_end.display_frame()
        end = my_end.input_box.end
    name = my_end.input_box.text
    print(name)
    return name

if __name__ == "__main__":
    print(main())
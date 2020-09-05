import pygame
from pygame import display, font, sprite, time, event
import color
import configuration
from audio_source import AudioSource
from game_object.player import Player
from coin_model_factory import CoinModelFactory
from scene.scene import Scene


class Game(Scene):
    def __init__(self):
        super().__init__()
        self._coin_model_factory = CoinModelFactory()
        self.__coin_list = self.__spawn_coins()
        self.__wall_list = self.__create_maze()
        self.__player = Player(color.YELLOW)
        self.__group = sprite.Group(self.__player)
        self.__ghost_group = sprite.Group()
        self.__font_score = font.Font('data/dpcomic.ttf',30)
        self._state = {'continue':False, 'exit':False,'win':False}
        
    def process(self):
        for e in event.get():
            if e.type == pygame.QUIT:
                self._state['exit'] = True
            self.__player.check_input(e)
        self.__player.update(self.__wall_list)
        
    def display_frame(self):
        self._clock.tick(self._fps)
        self.screen.fill(color.BLACK)
        
        for wall in self.__wall_list:
            wall.draw(self.screen)
        self.__group.draw(self.screen)
        display.flip()
        
    def __update_speed(self):
        pass
    def __spawn_ghost(self):
        pass
    def __spawn_coins(self):
        return []
    def __create_maze(self):
        return []
    
    def get_state(self):
        return self._state
    def get_clock(self):
        return self._clock

def main():
    pygame.init()
    myGame = Game()
    while not myGame.get_state()['exit']:
        myGame.process()
        myGame.display_frame()

if __name__ == "__main__":
    pass

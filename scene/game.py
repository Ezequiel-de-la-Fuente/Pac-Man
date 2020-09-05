import pygame
from pygame import display, font, sprite, time, event
import color
import configuration
from audio_source import AudioSource
from game_object.player import Player
from coin_model_factory import CoinModelFactory,Coin
from game_object.wall import Wall_two
from scene.scene import Scene


class Game(Scene):
    def __init__(self):
        super().__init__()
        self._coin_model_factory = CoinModelFactory()
        self.__coin_list = []
        self.__spawn_coins()
        
        self.__wall_group = sprite.Group()
        self.__create_maze()
        
        self.__player = Player(color.YELLOW)
        self.__group = sprite.Group(self.__player)
        
        self.__ghost_group = sprite.Group()
        self.__font_score = font.Font('data/dpcomic.ttf',30)
        self._state = {'continue':False, 'exit':False,'win':False}
        
    def process(self):
        self.__wall_group.update()
        for e in event.get():
            if e.type == pygame.QUIT:
                self._state['exit'] = True
            self.__player.check_input(e)
        self.__player.update(self.__wall_group)
        self.__check_colisions()
        
    def display_frame(self):
        self._clock.tick(self._fps)
        self.screen.fill(color.BLACK)
        self.__wall_group.draw(self.screen)
        for coin in self.__coin_list:
            coin.draw(self.screen)
        self.__group.draw(self.screen)
        display.flip()
    
    def __check_colisions(self):
        index=0
        for e in self.__coin_list:
            if self.__player.rect.colliderect(e.get_rect()):
                print("Me choco una moneda {}".format(e.coin_model.color))
                e.play_sound()
                self.__coin_list.pop(index)
            index+=1
    
    def __update_speed(self):
        pass
    def __spawn_ghost(self):
        pass
    def __spawn_coins(self):
        pass
    def __create_maze(self):
        pass
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

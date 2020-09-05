import pygame
from pygame import display, font, sprite, time, event
import color
import configuration
from audio_source import AudioSource
from game_object.player import Player
from coin_model_factory import CoinModelFactory,Coin
from game_object.wall import Wall
from scene.scene import Scene


class Game(Scene):
    def __init__(self, level : str):
        super().__init__()
        self._coin_model_factory = CoinModelFactory()
        self.__coin_list = []
        self.__spawn_coins()
        
        self.__wall_group = sprite.Group()
        # self.__create_maze()
        self.load_level(level)
        
        self.__player = Player(color.YELLOW,x=30,y=30)
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
        #bottom_mid_left => A
        for index_i in range(2):
            for index_j in range(3):
                self.__wall_group.add(Wall('data/sprite/wall/wall_1.png',pos=(-100*index_i,375 - 25*index_j)))
                self.__wall_group.add(Wall('data/sprite/wall/wall_1.png',pos=(configuration.SCREEN_WIDTH - 75 + 50 * index_i,375 - 25*index_j)))
                
        #bottom_mid_left => A
        for index_i in range(2):
            for index_j in range(3):
                self.__wall_group.add(Wall('data/sprite/wall/wall_1.png',pos=(24 - 50*index_i,200 + 25*index_j)))
                self.__wall_group.add(Wall('data/sprite/wall/wall_1.png',pos=(configuration.SCREEN_WIDTH - 75 + 50 * index_i,200 + 25*index_j)))
        
        
    def get_state(self):
        return self._state
    def get_clock(self):
        return self._clock
    
    def load_level(self,level:str):
        x = y = 0
        y_coin = 5
        for row in level:
            for col in row:
                if col == "W":
                    self.__wall_group.add(Wall('data/sprite/wall/wall_0.png',pos=(x,y)))
                if col == "C" or col ==" ":
                    self.__coin_list.append(Coin(self._coin_model_factory.get_coin_model('white_coin_model'),pos=(x,y_coin),score=5))
                x += 25
                
            y += 25
            y_coin += 25
            x = 0

def main():
    level = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W               W              W",
        "W WW WWW WWWWWW W WWWWW WWW WW W",
        "W WW WWW WWWWWW W WWWWW WWW WW W",
        "W                              W",
        "W WWWW W WWWWWWWWWWWWWW W WWWW W",
        "W      W                W      W",
        "WWW WW WWWWW   WW   WWWWW WW WWW",
        "WWW WW W       WW       W WW WWW",
        "WWW WW W  WWWWWWWWWWWW  W WW WWW",
        "W   WW W                W WW   W",
        "            WW____WW            ",
        "W      W WW W______W WW W     WW",
        "WWW WW W WW W______W WW W WW WWW",
        "WWW WW W WW WWWWWWWW WW W WW WWW",
        "WWW WW W WW          WW W WW WWW",
        "WWW WW W WW WWWWWWWW WW W WW WWW",
        "W                              W",
        "W WWWW W WWWWWWWWWWWWWW W WWWW W",
        "W                              W",
        "W WW WWW WWWWWW W WWWWW WWW WW W",
        "W WW WWW WWWWWW W WWWWW WWW WW W",
        "W        W            W        W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
    ]
    #24 filas
    #32 columnas
    pygame.init()
    myGame = Game(level)
    while not myGame.get_state()['exit']:
        myGame.process()
        myGame.display_frame()

if __name__ == "__main__":
    pass

import pygame
from pygame import sprite, image, transform
from game_object.coin_model import CoinModel
from game_object.coin import Coin
import color
class CoinModelFactory():
    _NORMAL_SCALE = (10,10)
    _BIG_SCALE = (25,25)
    def __init__(self):
        self.__red_coin_model = CoinModel(color.RED,CoinModelFactory._NORMAL_SCALE)
        self.__yellow_coin_model = CoinModel(color.YELLOW,CoinModelFactory._NORMAL_SCALE)
        self.__yellow_big_coin_model = CoinModel(color.YELLOW,CoinModelFactory._BIG_SCALE)
        self.__blue_coin_model = CoinModel(color.BLUE,CoinModelFactory._NORMAL_SCALE)
        
    def get_coin_model(self, type : str):
        if type == 'red_coin_model':
            return self.__red_coin_model
        elif type == 'yellow_coin_model':
            return self.__yellow_coin_model
        elif type == 'yellow_big_coin_model':
            return self.__yellow_big_coin_model
        elif type == 'blue_coin_model':
            return self.__blue_coin_model
        else:
            raise ValueError('[WARNING]The type don`t exists.')
    
    @staticmethod
    def get_list_of_types():
        return ['red_coin_model','yellow_coin_model','yellow_big_coin_model','blue_coin_model']
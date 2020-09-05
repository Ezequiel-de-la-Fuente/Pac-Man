import pygame
from pygame import event, display, draw, sprite, time
import configuration, color
from game_object.player import Player
from game_object.coin_model import CoinModel
from game_object.coin import Coin
from coin_model_factory import CoinModelFactory
import scene.game

from scene.game import Game
import random
def main():
    pygame.init()
    done = False
    screen = display.set_mode(size=(configuration.SCREEN_WIDTH,configuration.SCREEN_HEIGHT))
    clock = time.Clock()
    
    player = Player((200,0,100))
    
    coin_model_factory = CoinModelFactory()
    coinList=[]
    
    for i in range(50):
        coinModel = None
        pos_x = random.randint(0,configuration.SCREEN_WIDTH)
        pos_y = random.randint(0,configuration.SCREEN_HEIGHT)
        if i == 10:
            coinModel = coin_model_factory.get_coin_model('red_coin_model')
        elif i == 20:
            coinModel = coin_model_factory.get_coin_model('blue_coin_model')
        elif i == 30:
            coinModel = coin_model_factory.get_coin_model('yellow_big_coin_model')
        else:
            coinModel = coin_model_factory.get_coin_model('yellow_coin_model')
        coin_aux = Coin(coinModel,(pos_x, pos_y),5)
        coinList.append(coin_aux)
    
    all_sprite = sprite.Group()
        
    wall_list = []
    wall_list.append(Wall(color.BLACK,pos=(100,200),tam=(20,300)))
    
    all_sprite.add(player)
    
    
    while not done:
        clock.tick(60)
        for e in event.get():
            if e.type == pygame.QUIT:
                done = True
            player.check_input(e)
        
        
        
        screen.fill(color.WHITE)
        player.update(wall_list)
           
        
        for e in wall_list:
            e.draw(screen)
            
        all_sprite.draw(screen)
        
        for e in coinList:
            e.draw(screen)
        
        index=0
        for e in coinList:
            if player.rect.colliderect(e.get_rect()):
                print("Me choco una moneda {}".format(e.coin_model.color))
                e.play_sound()
                coinList.pop(index)
            index+=1

        
        display.flip()


if __name__ == "__main__":
    # main()
    scene.game.main()
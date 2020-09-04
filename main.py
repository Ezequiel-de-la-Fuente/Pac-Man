import pygame
from pygame import event, display, draw, sprite, time
import configuration, color
from game_object.player import Player
from game_object.coin_model import CoinModel
from game_object.coin import Coin

import random
def main():
    pygame.init()
    done = False
    screen = display.set_mode(size=(configuration.SCREEN_WIDTH,configuration.SCREEN_HEIGHT))
    clock = time.Clock()
    
    player = Player((200,0,100))
    
    coinModel = CoinModel((255,255,0),(10,10))
    coinList=[]
    for i in range(50):
        pos_x = random.randint(0,configuration.SCREEN_WIDTH)
        pos_y = random.randint(0,configuration.SCREEN_HEIGHT)
        coin_aux = Coin(coinModel,(pos_x, pos_y),5)
        coinList.append(coin_aux)
    
    all_sprite = sprite.Group()
    all_sprite.add(player)
    while not done:
        clock.tick(60)
        for e in event.get():
            if e.type == pygame.QUIT:
                done = True
            player.check_input(e)
        
        # all_sprite.update(wal)
        
        
        screen.fill(color.WHITE)
        player.update(walls=[])
           
        
        
        all_sprite.draw(screen)
        for e in coinList:
            e.draw(screen)
        index=0
        for e in coinList:
            if player.rect.colliderect(e.get_rect()):
                print("Me choco {}".format(e.id))
                e.play_sound()
                coinList.pop(index)
            index+=1

        
        display.flip()


if __name__ == "__main__":
    main()
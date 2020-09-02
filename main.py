import pygame
from pygame import event, display, draw, sprite, time
import configuration, color
from game_object.player import Player

def main():
    pygame.init()
    done = False
    screen = display.set_mode(size=(configuration.SCREEN_WIDTH,configuration.SCREEN_HEIGHT))
    clock = time.Clock()
    
    player = Player((200,0,100))
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
        
        # aux=pygame.draw.rect(screen, (0, 100, 255), (50, 50, 162, 300), 3)  # width = 3
        player.update(walls=[])
           
        
        
        all_sprite.draw(screen)
        display.flip()


if __name__ == "__main__":
    main()
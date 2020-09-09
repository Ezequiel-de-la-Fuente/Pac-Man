import pygame
from pygame import sprite, image
import configuration

class DeadGhostModel():
    def __init__(self):
        self.images = []
        for i in range(4):
            self.images.append(image.load('data\\sprite\\ghost\\dead\\dead_ghost_{}.png'.format(i)))
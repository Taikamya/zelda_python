import pygame, sys
from settings import *

class Tile(pygame.sprite.Sprite):
    # init method
    def __init__(self, pos, groups) -> None:
        super().__init__(groups)

        self.image = pygame.image.load('./assets/graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

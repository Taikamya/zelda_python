import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self) -> None:
        
        # get the display_surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for idy, row in enumerate(WORLD_MAP):
            for idx, col in enumerate(row):
                x = idx * TILESIZE
                y = idy * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    Player((x, y), [self.visible_sprites])


    def run(self):
        # update and draw game
        self.visible_sprites.draw(self.display_surface)

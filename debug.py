import pygame
import logging

# initializing pygame
pygame.init()

# selected font
font = pygame.font.Font(None, 30)

# defining debug function
def debug(info, y = 10, x = 10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x, y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)

    # logging debugs
    logging.debug("debug info: ")
    logging.info("info msg: ")
    logging.error("error: ")
    level = logging.DEBUG
    fmt = "[%(levelname)s] %(asctime)s - %(message)s"
    logging.basicConfig(level=level, format=fmt)

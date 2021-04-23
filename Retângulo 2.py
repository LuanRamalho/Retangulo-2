# -*- coding: utf-8 -*-
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (0,5,157)
LIGHT_GREEN = (111,255,109)
GREEN = (0, 255, 0)
DARK_GREEN = (0,102,2)
LIGHT_RED = (255, 111, 97)
RED = (255, 0, 0)
DARK_RED = (137, 2, 0)
LIGHT_CYAN = (0, 255, 255)
CYAN = (0, 133, 244)
DARK_CYAN = (0,65,132)
GREENISH_YELLOW = (181,255,14)
YELLOW = (255, 255, 0)
DARK_YELLOW = (168, 165, 0)
ORANGE = (255, 116, 3)
DARK_ORANGE = (143, 64, 0 )
PURPLE = (117, 0, 244)
DARK_PURPLE = (64, 0, 113)
PINK = (240, 0, 236)
DARK_PINK = (168, 0, 166)
BROWN = (150, 75, 0)
LIGHT_GRAY = (210, 210, 210)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

pygame.init()


janela = pygame.display.set_mode((700,600))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    janela.fill((WHITE))

    # desenhando na superfície
    pygame.draw.rect(janela, RED, [20, 50, 25, 75])
    pygame.draw.rect(janela, BLUE, [200, 210, 40, 20])
    pygame.draw.ellipse(janela, RED, [300, 200, 40, 40])
    pygame.draw.polygon(janela, GREEN, [[420, 200], [440, 240], [400, 240]])
    pygame.draw.rect(janela, CYAN, [250, 300, 30, 100])
    pygame.draw.rect(janela, DARK_ORANGE, [400, 300, 30, 100])
    pygame.draw.rect(janela, GREENISH_YELLOW, [325, 300, 30, 100])
    pygame.draw.rect(janela, PURPLE, [650, 50, 25, 75])
    pygame.draw.rect(janela, DARK_CYAN, [350,50,25,75])

    pygame.display.flip()





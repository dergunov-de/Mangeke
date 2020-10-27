# Занятие 6
import pygame
import os
BLUE = (0, 0, 75)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
W = 800
H = 600
pygame.init()
pygame.display.set_caption('Текст')
screen = pygame.display.set_mode((W, H))
font = pygame.font.SysFont('Arial', 56, True, False)
font_box = pygame.Surface((W - 20, font.get_height()))
font_rect = font_box.get_rect(center=(W // 2, H - font.get_height()))
font2 = pygame.font.SysFont('Arial', 28, False, True)
screen.fill(BLUE)
text1 = 'Всем привет'
pos = (200, 200)
screen.blit(font.render(text1, True, WHITE), (pos[0] + 5, pos[1] + 5))
text2 = 'Задание на урок'
pos = (265, 280)
screen.blit(font2.render(text2, True, YELLOW), (pos[0] + 5, pos[1] + 5))


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()

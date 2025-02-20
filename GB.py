import pygame
import random

pygame.init()

screen_width = 1350
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Burger Falling on School!')

WHITE = (255, 255, 255)

burger_img = pygame.image.load('burger.jpeg')
school_bg = pygame.image.load('018_billhogarth_3.jpeg')

burger_img = pygame.transform.scale(burger_img, (250, 250))
school_bg = pygame.transform.scale(school_bg, (screen_width, screen_height))

burger_width = 250
burger_x = (screen_width - burger_width) // 2 
burger_y = -burger_width 
burger_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    burger_y += burger_speed
    if burger_y > screen_height:
        burger_y = -burger_width  
        burger_x = (screen_width - burger_width) // 2  

    screen.fill(WHITE)
    screen.blit(school_bg, (0, 0))
    screen.blit(burger_img, (burger_x, burger_y))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
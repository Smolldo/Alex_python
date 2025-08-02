import pygame

pygame.init()

import random
screen = pygame.display.set_mode((1280, 720))

x, y = 400, 300
speed = 5


running = True

while running:
    keys = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                y -= speed
            elif e.key == pygame.K_DOWN:
                y += speed
            elif e.key == pygame.K_LEFT:
                x -= speed
            elif e.key == pygame.K_RIGHT:
                x += speed

    if keys[pygame.K_LCTRL] or  keys[pygame.K_RCTRL]:
        if keys[pygame.K_c]:
            screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            pygame.display.flip()

    
            


pygame.quit()
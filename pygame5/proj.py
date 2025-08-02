import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

bg = pygame.image.load('pygame5/bg.jpg')
bg_scaled = pygame.transform.scale(bg, (800,600))

running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.blit(bg_scaled, (0, 0))

    pygame.display.flip()
import pygame
import sys

screen = pygame.display.set_mode((800, 600))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
color_index = 0

stand_img = pygame.image.load('pygame5/img1.png')
jump_img = pygame.image.load('pygame5/img2.png')



x, y = 100, 300
is_jumping = False
jump_height = 0
max_jump = 50

clock = pygame.time.Clock()
fps = 60

ANIMATION_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ANIMATION_EVENT, 200)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == ANIMATION_EVENT:
            color_index = (color_index + 1)  % len(colors)
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                jump_height = max_jump

    if is_jumping:
        y -= 5
        jump_height -= 5
        if jump_height <= 0:
            is_jumping = False
    else:
        if y < 300:
            y += 5

    screen.fill(WHITE)
    if is_jumping:
        screen.blit(stand_img, (x, y))
    else:
        screen.blit(jump_img, (x, y))

    # pygame.draw.rect(screen, colors[color_index], (300 , 200, 50, 50))
    # x += speed
    # if x > 800:
    #     x = -50

    pygame.display.flip()
    clock.tick(fps)
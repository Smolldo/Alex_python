import pygame
# import time

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('My first game')

running = True
x_position = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), (x_position, 300, 50, 50))
    pygame.display.flip()

    x_position += 5 
    if x_position > 1280:
        x_position = 0

    pygame.time.delay(50)

    # pygame.draw.line(screen, (255,255,255), (100, 100), (700,500), 5)
    # pygame.draw.circle(screen, (255,0,255), (400,300), 100, 5)
    # pygame.display.flip()

# icon_image = pygame.image.load('pygame1/steve.png')
# pygame.display.set_icon(icon_image)


# screen.fill((0,0,255))
# font = pygame.font.Font(None, 36)
# text = font.render('Hello gamers', True, (255,255,255))
# screen.blit(text, (50,50))


# pygame.display.flip()

# time.sleep(5)
pygame.quit()
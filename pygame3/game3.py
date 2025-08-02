import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

running = True
square1 = pygame.Rect(350, 250, 100, 100)
square2 = pygame.Rect(150, 150, 100, 100)
# dragging = False
color1 = (0,128, 255)
color2 = (255,0,0)

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        # elif e.type == pygame.MOUSEBUTTONDOWN:
        #     if e.button == 1:
        #         print('LKM')
        #     elif e.button == 2:
        #         print('SKM')
        #     elif e.button == 3:
        #         print('PKM')
        # elif e.type == pygame.MOUSEMOTION:
        #     mouse_pos = e.pos
        #     print(mouse_pos)
        # mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)

        # screen.fill((255,255,255))

        # font = pygame.font.Font(None, 36)
        # text = font.render(f'позиція мишки: {mouse_pos}', True, (0,0,0))
        # screen.blit(text, (20, 20))

        # pygame.display.flip()
    #     elif e.type == pygame.MOUSEBUTTONDOWN:
    #         if square.collidepoint(e.pos):
    #             dragging = True
    #             mouse_x, mouse_y = e.pos
    #             offset_x = square.x - mouse_x
    #             offset_y = square.y - mouse_y

    #     elif e.type == pygame.MOUSEBUTTONUP:
    #         dragging = False

    #     elif e.type == pygame.MOUSEMOTION:
    #         if dragging:
    #                 mouse_x, mouse_y = e.pos
    #                 square.x = mouse_x + offset_x
    #                 square.y = mouse_y + offset_y

    # screen.fill((255,255,255))
    # pygame.draw.rect(screen, (0, 128, 255), square)
    # pygame.display.flip()

        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                square1.x -= 10
            elif e.key == pygame.K_RIGHT:
                square1.x += 10
            elif e.key == pygame.K_UP:
                square1.y -= 10
            elif e.key == pygame.K_DOWN:
                square1.y += 10

    if square1.colliderect(square2):
        color1 = (0,255, 0)
    else:
        color1 = (0,128,255)

    screen.fill((255,255,255))
    pygame.draw.rect(screen, color1, square1)
    pygame.draw.rect(screen, color2, square2)
    pygame.display.flip()

pygame.quit()
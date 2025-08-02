import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
image = pygame.image.load('pygame4/MGS2_Solid_Snake.png')
scaled_image = pygame.transform.scale(image, (100, 100))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# WHITE = (255,255,255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)

# player = pygame.Rect(100, 100, 50, 50)
# obstacle = pygame.Rect(300, 300, 50, 50)
# goal = pygame.Rect(600, 400, 50, 50)

# speed = 1
# score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    screen.fill((255,255,255))
    all_sprites.draw(screen)
    pygame.display.flip()
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     player.x -= speed
    # if keys[pygame.K_RIGHT]:
    #     player.x += speed
    # if keys[pygame.K_UP]:
    #     player.y -= speed
    # if keys[pygame.K_DOWN]:
    #     player.y += speed

    # if player.colliderect(obstacle):
    #     player.x, player.y = 100, 100
    #     score = 0
    # elif player.colliderect(goal):
    #     goal.x, goal.y = 700, 500
    #     score += 1


    # screen.fill(WHITE)
    # pygame.draw.rect(screen, GREEN, player)
    # pygame.draw.rect(screen, RED, obstacle)
    # pygame. draw.rect(screen, YELLOW, goal)

    # font = pygame.font.Font(None, 36)
    # text = font.render(f'Score: {score}', True, BLUE)
    # screen.blit(text, (10, 10))

    # pygame.display.flip()



pygame.quit()
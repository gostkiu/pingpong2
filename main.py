import pygame

WIDTH = 1300
HEIGHT = 700
SIZE = (WIDTH,HEIGHT)
FPS = 60













w = pygame.display.set_mode(SIZE)
backgraund = pygame.transform.scale(pygame.image.load("skyline.jpg"),SIZE)

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    w.blit(backgraund,(0,0))

    pygame.display.update()
    clock.tick(FPS)


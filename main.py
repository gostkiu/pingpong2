import pygame

WIDTH = 1300
HEIGHT = 700
SIZE = (WIDTH,HEIGHT)
FPS = 60













w = pygame.display.set_mode(SIZE)
background = (0,0,0)
w.fill(background)
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()
    clock.tick(FPS)


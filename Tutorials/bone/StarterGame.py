import pygame

pygame.init()

pygame.display.set_mode((800, 600))
pygame.display.set_caption('Don''t even think about Jim Dress')

clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

            print(event)

    pygame.display.update()
    clock.tick(60)
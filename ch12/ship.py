import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image = pygame.image.load('./image/ship.bmp')
rect = image.get_rect()

while True: # 계속 도는것
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit # sys import 시켜야함   

    # Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    screen.blit(image,rect)
    # ...

    pygame.display.flip()  # Refresh on-screen display 
    clock.tick(60)         # wait until next frame (at 60 FPS) 1분에 60번 클릭 무한히 돌고 60번 클릭한다는 건 고정값이다?
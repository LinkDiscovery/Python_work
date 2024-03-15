import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
image = pygame.image.load('./image/ship.bmp')
ship_rect = image.get_rect()

# image_rect.left = 1280/2
# image_rect.top = 600

ship_rect.midbottom = screen.get_rect().midbottom


WidTH = 1280/2
Height = 720/2
new_var1 = "purple"

rect = pygame.Rect((WidTH, Height), (400, 400))
# rect = screen.get_rect() 위에꺼와 같은거다. # rect를 받는 방법
# rect = image.get_rect()


def create_bullet(ship_rect):
    bullet = pygame.Rect(0,0,3,10)
    bullet.midtop = ship_rect.midtop
    return bullet

bullets = []
bullet = create_bullet(ship_rect)
bullets.append(bullet)
BULLET_COLOR = (255,0,0)



while True: # 계속 도는것
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit # sys import 시켜야함   
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_rect.x -= 5
            elif event.key == pygame.K_RIGHT:
                ship_rect.x += 5
            elif event.key == pygame.K_UP:
                ship_rect.y -= 5
            elif event.key == pygame.K_DOWN:
                ship_rect.y += 5
            elif event.key == pygame.K_SPACE:
                create_bullet(create_bullet(ship_rect))
            

    # Do logical updates here.
    # ...
    for bullet in bullets:
        bullet.top = -1
        
    
    screen.fill(new_var1)  # Fill the display with a solid color

    # Render the graphics here.
    
    screen.blit(image, ship_rect)
    for bullet in bullets:
        pygame.draw.rect(screen,BULLET_COLOR,bullet)
    
    # ...

    
    pygame.display.flip()  # Refresh on-screen display 
    new_var = 30
    clock.tick(new_var)         # wait until next frame (at 60 FPS) 1분에 60번 클릭 무한히 돌고 60번 클릭한다는 건 고정값이다?